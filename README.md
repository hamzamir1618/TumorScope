# TumorScope

TumorScope is a deep learning project for tumor classification using ResNet18.  
The project includes scripts and notebooks for data organization, preprocessing, training, evaluation, and visualization of results.

---

## Project Structure

```

TumorScope/
│
├── tumorscope.ipynb        # Notebook to load, train, and save model (ResNet18)
├── newtesting.ipynb        # Notebook to test & evaluate using trained model
│
├── organize.py             # Organizes full dataset into yes/no subfolders
├── organize_sample.py      # Organizes a smaller sample dataset (for quick testing)
├── split.py                # Splits cleaned dataset into train/val/test folders
│
├── best_model.pth          # Trained model (placeholder, link below)
├── testing_data           # Raw dataset (placeholder, link below)
└── README.md
```

---

## Workflow

1. **Dataset Preparation**
   - Use `organize.py` to structure the full dataset into:
     ```
     dataset_cleaned/
     ├── yes/
     └── no/
     ```
   - Use `organize_sample.py` if you want to prepare only a smaller subset:
     ```
     dataset_sampled/
     ├── yes/
     └── no/
     ```

2. **Data Splitting**
   - Run `split.py` to divide the cleaned dataset into:
     ```
     dataset_cleaned_split/
     ├── train/
     ├── val/
     └── test/
     ```

3. **Model Training**
   - Open `tumorscope.ipynb`
   - Loads ResNet18, trains on the dataset, and saves the best model as `best_model.pth`.

4. **Model Testing & Evaluation**
   - Open `newtesting.ipynb`
   - Loads the trained model (`best_model.pth`)
   - Evaluates performance on the test set
   - Displays results (accuracy, metrics, and visualizations)

---

## Resources

- Trained Model (`best_model.pth`): [Google Drive Link Here]
- Raw Dataset (`testing_data`): [Google Drive Link Here]

(Replace with actual links once uploaded)

---

## Dependencies

TumorScope requires the following Python packages:

- **Core**
  - `torch`
  - `torchvision`
  - `numpy`
  - `matplotlib`
  - `Pillow`

- **Data & Metrics**
  - `scikit-learn`

- **Visualization**
  - `pytorch-grad-cam` (for Grad-CAM visualizations)

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/hamzamir1618/TumorScope.git
   cd TumorScope


2. Install dependencies:

   ```bash
   pip install torch torchvision scikit-learn matplotlib Pillow pytorch-grad-cam
   ```

3. Download the dataset and model from the links above, and place them in the project folder.

4. Run notebooks in order:

   * `tumorscope.ipynb` (Training)
   * `newtesting.ipynb` (Evaluation)

---

## Notes

* `organize.py` expects the raw dataset in the `testing_data/` folder.
* `split.py` assumes the organized dataset is in `dataset_cleaned/`.
* The trained model is automatically saved as `best_model.pth` after training.

---

## Contributing

Feel free to open issues or pull requests to improve TumorScope :)

---

