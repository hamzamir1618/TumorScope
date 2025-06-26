import os
import shutil

# === Paths ===
original_dataset_path = 'D:\\OFFICE WORK\\KDD Summer 2025\\task3\\testing_data'  # Change this
output_path = 'dataset_cleaned'  # Will be created in current dir

# Create destination folders
os.makedirs(os.path.join(output_path, 'yes'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'no'), exist_ok=True)

# Helper function to copy images
def copy_images(src_folder, label):
    dest_folder = os.path.join(output_path, label)
    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                src_file = os.path.join(root, file)
                new_name = f"{label}_{len(os.listdir(dest_folder))+1:05d}" + os.path.splitext(file)[1]
                dst_file = os.path.join(dest_folder, new_name)
                shutil.copy2(src_file, dst_file)

# === Walk through Training and Testing ===
for split in ['Training', 'Testing']:
    split_path = os.path.join(original_dataset_path, split)
    for class_folder in os.listdir(split_path):
        class_path = os.path.join(split_path, class_folder)
        if not os.path.isdir(class_path):
            continue
        if class_folder.lower() == 'no_tumor':
            copy_images(class_path, 'no')
        else:
            copy_images(class_path, 'yes')

print("✅ Dataset has been cleaned and reorganized into 'yes' and 'no' folders.")
