#pip install torch transformers pillow

import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os
import h5py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Set device (GPU if available)
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")  # Force CPU usage
model.to(device)

# Encode an image
def encode_image(image_path):
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    return image_features.cpu().numpy()  # Convert to numpy array

# Encode text
def encode_text(text):
    inputs = processor(text=text, return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        text_features = model.get_text_features(**inputs)
    return text_features.cpu().numpy()  # Convert to numpy array

# Store image embeddings in HDF5 format
def save_embeddings_to_hdf5(image_folder, output_file="image_embeddings.h5"):
    with h5py.File(output_file, "w") as f:
        # Create a dataset for the embeddings and image names
        image_names = []
        embeddings = []
        
        for image_name in os.listdir(image_folder):
            image_path = os.path.join(image_folder, image_name)
            embedding = encode_image(image_path)
            
            image_names.append(image_name)
            embeddings.append(embedding)
        
        # Convert to numpy arrays
        image_names = np.array(image_names, dtype="S")
        embeddings = np.array(embeddings)
        
        # Store the image names and embeddings as datasets in the HDF5 file
        f.create_dataset("image_names", data=image_names)
        f.create_dataset("embeddings", data=embeddings)

# Retrieve top-K images based on a text query
def retrieve_top_k_images(text_query, hdf5_file, k=5):
    with h5py.File(hdf5_file, "r") as f:
        image_names = f["image_names"][:]
        embeddings = f["embeddings"][:]
    
    # Encode the text query
    text_embedding = encode_text(text_query)

    # Compute similarity scores
    similarities = {}
    for i, image_name in enumerate(image_names):
        # Compute cosine similarity between text and image embeddings
        sim = cosine_similarity(text_embedding, embeddings[i].reshape(1, -1))[0][0]  # Reshape for cosine similarity
        similarities[image_name.decode()] = sim  # Decode byte strings to regular strings

    # Sort by similarity and get top-K images
    sorted_images = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]
    return [image_name for image_name, _ in sorted_images]


## Example usage
#image_folder = "data/dataset_images"
#save_embeddings_to_hdf5(image_folder, "image_embeddings.h5")

## Retrieve top 3 images for a query
#text_query = "A bid in water"
#top_images = retrieve_top_k_images(text_query, "image_embeddings.h5", k=3)
#print(top_images)