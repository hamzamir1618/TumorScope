import splitfolders
import os

# Define the input and output directories
input_folder = "D:\\OFFICE WORK\\KDD Summer 2025\\task3\\brain_tumor_dataset"  # Replace with the path to your dataset folder containing 'yes' and 'no' subfolders
output_folder = "D:\\OFFICE WORK\\KDD Summer 2025\\task3\\split_dataset"  # Replace with where you want the split dataset

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Split the dataset into train (80%), validation (10%), and test (10%)
splitfolders.ratio(
    input_folder,
    output=output_folder,
    seed=42,  # For reproducibility
    ratio=(0.8, 0.1, 0.1),  # Train, Val, Test
    group_prefix=None  # Set to None for classification tasks
)

print("Dataset split completed! Check the output folder:", output_folder)