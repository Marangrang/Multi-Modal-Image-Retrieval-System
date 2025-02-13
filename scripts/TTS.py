from flask import Flask, render_template, request, jsonify
import pyttsx3
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

app = Flask(__name__, template_folder="../templates")

# Initialize the TTS engine
engine = pyttsx3.init()

# Load the BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_image_description(image_path):
    # Open the image
    raw_image = Image.open(image_path).convert("RGB")
    
    # Preprocess the image and generate a caption
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)
    
    return description

def speak_description(description):
    # Speak the generated description
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level
    engine.say(description)
    engine.runAndWait()

@app.route('/')
def home():
    return render_template('display_image.html')

@app.route('/speak', methods=['POST'])
def speak():
    description = request.json.get('description', '')
    if description:
        speak_description(description)
        return jsonify({"status": "success", "message": "Text-to-speech completed."}), 200
    return jsonify({"error": "No description provided."}), 400

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found."}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400
    if file:
        # Save the uploaded image temporarily
        image_path = "uploaded_image.jpg"
        file.save(image_path)
        
        # Generate the image description
        description = generate_image_description(image_path)
        
        # Speak the description
        speak_description(description)
        
        return jsonify({"status": "success", "description": description}), 200

if __name__ == '__main__':
    app.run(debug=True)
