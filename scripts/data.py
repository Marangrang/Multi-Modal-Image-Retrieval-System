#pip install kaggle
# Set Up Kaggle API Authentication
#mkdir -p ~/.kaggle
#mv /mnt/c/Users/NWUUSER/Downloads/kaggle.json ~/.kaggle/
#chmod 600 ~/.kaggle/kaggle.json  # Secure permissions

import kaggle
import zipfile
import os
import random
import shutil

# Define dataset details
KAGGLE_DATASET = "alessandrasala79/ai-vs-human-generated-dataset"
DEST_DIR = "data"  # Folder where the dataset will be stored
EXTRACT_DIR = os.path.join(DEST_DIR, "test_data_v2")  # Extract folder

# Ensure the destination folder exists
#os.makedirs(DEST_DIR, exist_ok=True)

# Download dataset using Kaggle API
#print("📥 Downloading dataset from Kaggle...")
#kaggle.api.dataset_download_files(KAGGLE_DATASET, path=DEST_DIR, unzip=True)

# Extract only 'test_data_v2' folder
#print("📦 Extracting necessary files...")
#if os.path.exists(EXTRACT_DIR):
#    print(f"✅ Data is already extracted in {EXTRACT_DIR}")
#else:
#    with zipfile.ZipFile(os.path.join(DEST_DIR, "ai-vs-human-generated-dataset.zip"), "r") as zip_ref:
#        zip_ref.extractall(DEST_DIR)
#    print(f"✅ Data extracted to {EXTRACT_DIR}")

# Optional: Remove the zip file to save space
zip_file_path = os.path.join(DEST_DIR, "ai-vs-human-generated-dataset.zip")
if os.path.exists(zip_file_path):
    os.remove(zip_file_path)
    print("🗑️ Removed zip file to save space.")
else:
    print("⚠️ No zip file found. Skipping deletion.")


print("🚀 Dataset is ready!")


###                        sample_500_images

# Define paths
SOURCE_FOLDER = "data/test_data_v2"  # Folder containing all images
DEST_FOLDER = "data/dataset_images"        # New folder for sampled images
SAMPLE_SIZE = 500                     # Number of images to sample

# Ensure the destination folder exists
os.makedirs(DEST_FOLDER, exist_ok=True)

# List all images in the source folder
all_images = [img for img in os.listdir(SOURCE_FOLDER) if img.endswith(('.png', '.jpg', '.jpeg'))]

# Check if we have enough images
if len(all_images) < SAMPLE_SIZE:
    print(f"⚠️ Not enough images! Found {len(all_images)} images, but need {SAMPLE_SIZE}.")
    SAMPLE_SIZE = len(all_images)  # Adjust to available count

# Randomly sample 500 images
sampled_images = random.sample(all_images, SAMPLE_SIZE)

# Copy sampled images to the new folder
for img in sampled_images:
    src_path = os.path.join(SOURCE_FOLDER, img)
    dest_path = os.path.join(DEST_FOLDER, img)
    shutil.copy(src_path, dest_path)

print(f"✅ Successfully copied {SAMPLE_SIZE} images to {DEST_FOLDER}!")
