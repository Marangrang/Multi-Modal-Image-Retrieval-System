#pip install flask 
#pip install ffmpeg
# pip install --upgrade whisper torch

from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from Feature_Extraction import retrieve_top_k_images
import whisper
import uuid

# Adjust paths since app.py is inside scripts/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Go one level up
IMAGE_FOLDER = os.path.join(BASE_DIR, "data", "dataset_images")  # Absolute path
TRANSCRIPTION_FOLDER = os.path.join(BASE_DIR, "transcription")

app = Flask(__name__, template_folder="../templates")

# Ensure the transcription folder exists
os.makedirs(TRANSCRIPTION_FOLDER, exist_ok=True)

# Load Whisper model
model = whisper.load_model("base")

# Function to transcribe audio using Whisper
def transcribe_audio(file_path):
    print(file_path)
    try:
        print(f"File path being passed: {file_path}")  # Log the path
        
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File does not exist at {file_path}")  # Log missing file
            return f"File not found at {file_path}"
        
        # Check file size
        file_size = os.path.getsize(file_path)
        print(f"File size: {file_size} bytes")
        
        # Transcribe the audio
        result = model.transcribe(file_path)
        print(f"Transcription result: {result}")
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}"
    
# Route to serve images from the dataset folder
@app.route('/dataset_images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')

    if not query:
        return jsonify({"error": "No query provided."}), 400

    # Retrieve top 3 images for the query
    top_images = retrieve_top_k_images(query, 'image_embeddings.h5', k=3)

    # Check if there are images returned
    if not top_images:
        return jsonify({"error": "No results found."})

    # Construct the URLs for the images
    image_urls = [f"/dataset_images/{image}" for image in top_images]

    return jsonify({"results": image_urls}), 200

# Route to handle audio transcription
@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Check if the 'audio' part is present in the request
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file part in the request."}), 400

        # Get the audio file from the request
        audio = request.files['audio']
        
        # If the user does not select a file, return an error
        if audio.filename == '':
            return jsonify({"error": "No selected file."}), 400
        
        # Generate a unique filename for the temporary audio file
        audio_filename = f"temp_audio_{uuid.uuid4().hex}.wav"
        
        # Create the full path to save the audio file inside the transcription folder
        audio_path = os.path.join(TRANSCRIPTION_FOLDER, audio_filename)
        
        # Save the audio file in the transcription folder
        audio.save(audio_path)

        # Check if the file is saved properly
        if not os.path.exists(audio_path):
            return jsonify({"error": "Audio file was not saved properly."}), 500

        # Transcribe the audio to text using Whisper
        text = transcribe_audio(audio_path)

        # Remove the temporary audio file after transcription
        #os.remove(audio_path)

        # Return the transcribed text as a JSON response
        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"error": f"An error occurred during transcription: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
