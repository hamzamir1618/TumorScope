import os
import shutil
import random

# === Paths ===
original_dataset_path = 'D:\\OFFICE WORK\\KDD Summer 2025\\task3\\testing_data'  # Change this
output_path = 'dataset_sampled'  # New sampled dataset
sample_size = 10  # Number of images per class

# Create destination folders
os.makedirs(os.path.join(output_path, 'yes'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'no'), exist_ok=True)

# === Accumulators for files ===
yes_images = []
no_images = []

# === Gather all image paths ===
for split in ['Training', 'Testing']:
    split_path = os.path.join(original_dataset_path, split)
    for class_folder in os.listdir(split_path):
        class_path = os.path.join(split_path, class_folder)
        if not os.path.isdir(class_path):
            continue

        image_list = [
            os.path.join(class_path, f)
            for f in os.listdir(class_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]

        if class_folder.lower() == 'no_tumor':
            no_images.extend(image_list)
        else:
            yes_images.extend(image_list)

# === Randomly sample ===
yes_sample = random.sample(yes_images, min(sample_size, len(yes_images)))
no_sample = random.sample(no_images, min(sample_size, len(no_images)))

# === Copy images to output ===
def copy_sampled_images(image_list, label):
    dest_folder = os.path.join(output_path, label)
    for i, src_file in enumerate(image_list, 1):
        ext = os.path.splitext(src_file)[1]
        dst_file = os.path.join(dest_folder, f"{label}_{i:05d}{ext}")
        shutil.copy2(src_file, dst_file)

copy_sampled_images(yes_sample, 'yes')
copy_sampled_images(no_sample, 'no')

print(f"✅ Sampled dataset created in '{output_path}' with {len(yes_sample)} tumor and {len(no_sample)} non-tumor images.")
