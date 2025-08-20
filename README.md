# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

# Stage 06 — Data Preprocessing

This stage focuses on applying data cleaning techniques to prepare raw datasets for analysis and modeling.  

---

## Steps Completed

### 1. Load Raw Dataset
- Import the raw CSV file into a pandas DataFrame.  
- Inspect the shape and preview the first rows to understand the structure.  

### 2. Apply Cleaning Functions
- **Fill missing values** using median strategy.  
- **Drop rows with missing values** when appropriate.  
- **Normalize numeric columns** to the range [0, 1].  

### 3. Save Cleaned Dataset
- Export the processed dataset to `/data/processed/`.  
- Ensure the file is reproducible and ready for further analysis.  

---

## Hypotheses

- Cleaning the dataset will reduce noise and improve model performance.  
- Normalization will make features comparable across scales.  
- Filling missing values with median should preserve distribution better than mean.  

---

## Reflections

### What worked well
- The cleaning functions (`fill_missing_median`, `drop_missing`, `normalize_data`) were reusable and modular.  
- Using a consistent preprocessing pipeline simplified debugging and ensured reproducibility.  

### What was challenging
- Managing different versions of the dataset (raw vs. processed) required careful file path handling.  
- Choosing between dropping vs. imputing missing values sometimes changed results significantly.  

### What I would improve next time
- Add logging or print statements to track each step of the preprocessing pipeline.  
- Automate the workflow so that running the notebook always produces the latest cleaned dataset.  
- Compare multiple imputation strategies (median vs. mean vs. mode) to test which performs best.  

---
