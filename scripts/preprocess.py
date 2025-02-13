import os
import whisper

# Check if FFmpeg is installed
os.system("ffmpeg -version")

# Path to the audio file
audio_path = r"C:\Users\NWUUSER\Documents\deploy SLI\Multi-Modal Image Retrieval System\transcription\temp_audio_fcf8114466324165a9947d25bdff9167.wav"

# Check if the file exists
if not os.path.exists(audio_path):
    print(f"Error: File not found at {audio_path}")
else:
    print(f"File found: {audio_path}")

    # Load Whisper model
    model = whisper.load_model("base")

    try:
        result = model.transcribe(audio_path)
        print(result["text"])
    except Exception as e:
        print(f"Error during transcription: {e}")

