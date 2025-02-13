# Multi-Modal Image Retrieval System

## Overview
The **Multi-Modal Image Retrieval System** is designed to process and retrieve images using advanced AI techniques. It supports:
- **Automatic Speech Recognition (ASR)** for voice-based image search.
- **Deep Learning & Computer Vision** for feature extraction.
- **Natural Language Processing (NLP)** for text-based queries.
- **Efficient Image Sampling** from large datasets.

## Features
✅ **Image Retrieval**: Search and retrieve images based on textual or audio queries.  
✅ **Speech-to-Text (ASR)**: Uses Whisper to transcribe audio inputs.  
✅ **Deep Learning Models**: Utilizes PyTorch and Hugging Face models for embeddings.  
✅ **Efficient Image Sampling**: Selects a subset of images for faster training.  
✅ **Dataset Handling**: Automates dataset downloads and processing.  

#### System Architecture 
🔹 Core Components & Data Flow

1. Text Encoder (CLIP)
   - Converts user input into an embedding.
2. Image Encoder (CLIP)
   - Generates embeddings for dataset images.
3. Vector Database (FAISS/Milvus)
   - Stores image embeddings and enables fast similarity search.
4. Retrieval Mechanism
   - Uses K-Nearest Neighbors (K-NN) to find the most relevant images.
5. Frontend UI (Streamlit/Flask)
   - Allows users to enter text queries and view retrieved images.

🛠️ Architecture Diagram

+--------------------+        +-----------------------+        +---------------------+
|    User Input     | ---->  |   Text Encoder (CLIP) | ---->  |   Text Embedding    |
+--------------------+        +-----------------------+        +---------------------+
                                     |                    
                                     v                    
+--------------------+        +-----------------------+        +---------------------+
|  Dataset Images   | ---->  |  Image Encoder (CLIP) | ---->  |   Image Embeddings  |
+--------------------+        +-----------------------+        +---------------------+
                                     |
                                     v
+----------------------------+       +--------------------------+
|    Vector Database (FAISS) | <-->  |    Retrieval (K-NN)      |
+----------------------------+       +--------------------------+
                                     |
                                     v
+----------------------+      +-------------------+
|   Retrieved Images   | ---> |  Frontend (UI)   |
+----------------------+      +-------------------+


### Frontend Integration 
- Framework: Use Flask + React for a more customizable interface.
- Features:
  - Text input box for queries.
  - Display of top-K retrieved images.
  - Real-time processing using CLIP.

### Bonus: Inclusive Design
To extend accessibility for visually impaired users:

- Voice Query Input: Use speech-to-text (STT) models like Whisper to allow voice-based search.


## Setup and Installation Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- [ffmpeg](https://ffmpeg.org/download.html) (required for audio processing)
- Kaggle API key (if downloading datasets)

### Steps for Setup

1. Clone the Repository


2. Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies Ensure you are in the project directory and then run:

pip install -r requirements.txt

Ensure FFmpeg is installed separately (not via pip).
Windows: Download from FFmpeg Official Site, extract, and add to PATH

### How to Run the System

#### Running the Application

Once you have installed the dependencies and set up the environment, you can run the system as follows:

1. Setting Up Kaggle API
- Get your Kaggle API key from Kaggle.
- mkdir -p ~/.kaggle
- mv download_folder/kaggle.json ~/.kaggle/
- chmod 600 ~/.kaggle/kaggle.json  

python scripts/data.py

2. Run the Main Application In your terminal, run:

python scripts/app.py

3. Running with Specific Configurations (if applicable) If your system requires configuration files or specific environment variables, make sure to specify them:

export CONFIG_PATH=/path/to/config
python scripts/app.py


#### File Structure

Multi-Modal-Image-Retrieval
│── data/                      # Stores dataset images
│   ├── dataset_images         # sample 500 images
│── scripts/                   # Processing scripts
│   ├── app.py                 # Handles dataset download & extraction
│   ├── data.py                # Selects a subset of images
│   ├── Feature_Extraction.py  # retrieve top k images
│   ├── TTS.py                 # Text To Speech
│── templates/                 # Stores HTML
│   ├── index.html             # HTML file
│── requirements.txt           # Dependencies
│── README.md                  # Documentation
