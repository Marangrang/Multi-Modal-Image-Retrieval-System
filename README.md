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

[Uploadin<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" version="26.0.12">
  <diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">
    <mxGraphModel dx="1120" dy="426" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-1" parent="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-2" value="" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;edgeStyle=orthogonalEdgeStyle;" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-3" target="WIyWlLk6GJQsqaUBKTNV-6" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-3" value="User Input" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="40" y="80" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-16" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-6" target="WIyWlLk6GJQsqaUBKTNV-10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-18" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-6" target="WIyWlLk6GJQsqaUBKTNV-7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-6" value="&lt;div&gt;&lt;br&gt;&lt;/div&gt;Text Encoder (CLIP)" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;align=center;strokeWidth=1;spacing=6;spacingTop=-4;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="200" y="60" width="100" height="80" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-7" value="Text Embedding" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="330" y="80" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-17" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-10" target="WIyWlLk6GJQsqaUBKTNV-12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-19" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-10" target="WIyWlLk6GJQsqaUBKTNV-11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-10" value="&lt;div&gt;&lt;br&gt;&lt;/div&gt;Image Encoder (CLIP)" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;align=center;strokeWidth=1;spacing=6;spacingTop=-4;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="200" y="200" width="100" height="80" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-11" target="tO4XE-NyFzzd2oOqjGNP-4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-14" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-11" target="tO4XE-NyFzzd2oOqjGNP-12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-11" value="Retrieval (K-NN)" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="250" y="340" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-12" value="Image Embeddings" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="340" y="220" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="tO4XE-NyFzzd2oOqjGNP-0" target="WIyWlLk6GJQsqaUBKTNV-10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-0" value="Dataset Images" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="40" y="220" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="210" y="360" as="sourcePoint" />
            <mxPoint x="210" y="360" as="targetPoint" />
            <Array as="points">
              <mxPoint x="210" y="360" />
              <mxPoint x="210" y="360" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="tO4XE-NyFzzd2oOqjGNP-4" target="WIyWlLk6GJQsqaUBKTNV-11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-4" value="Vector Database (FAISS)" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="40" y="340" width="160" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-12" value="Fronted (UI)" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="250" y="440" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-15" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="tO4XE-NyFzzd2oOqjGNP-13" target="tO4XE-NyFzzd2oOqjGNP-12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="tO4XE-NyFzzd2oOqjGNP-13" value="Retrieved Images" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="40" y="440" width="120" height="40" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
g Architecture Diagram.drawio…]()


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
   
git clone https://github.com:Marangrang/Multi-Modal-Image-Retrieval-System.git

cd Multi-Modal-Image-Retrieval

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
