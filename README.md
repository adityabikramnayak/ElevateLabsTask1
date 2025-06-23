# ElevateLabsTask1
Completed objectives mentioned in task 1 for ElevateLabs Internship
# Task 1 - Data Cleaning & Preprocessing (Titanic Dataset)

## 🎯 Objective
Clean and prepare the Titanic dataset to make it suitable for machine learning models by handling missing values, encoding categorical variables, standardizing numerical features, and identifying outliers.

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## ✅ Steps Performed

1. **Loaded Dataset**
   - Used `pandas.read_csv()` to load the dataset.

2. **Handled Missing Values**
   - Filled missing `Age` values with the median.
   - Filled missing `Embarked` values with the mode.
   - Dropped the `Cabin` column due to too many missing entries.

3. **Encoded Categorical Columns**
   - Converted `Sex` to binary (male = 1, female = 0).
   - One-hot encoded `Embarked` into `Embarked_Q` and `Embarked_S`.

4. **Standardized Numerical Features**
   - Applied Z-score standardization to `Age` and `Fare`.

5. **Visualized Outliers**
   - Used boxplots for `Age` and `Fare` to visualize outliers.

6. **Verified Clean Data**
   - Checked for remaining missing values (all handled).
   - Printed final data sample.

## 📦 Output
- Cleaned, encoded, and scaled Titanic dataset ready for machine learning.
- Output file: `cleaned_titanic.csv`

## 📁 Files in this Repo
- `Task1.py` – Python script for preprocessing
- `cleaned_titanic.csv` – Final cleaned dataset
- `README.md` – Description of task and steps followed

## 🔗 Dataset Source
[Titanic Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

---

**Submitted for:** AI & ML Internship (Task 1 – Data Cleaning & Preprocessing)
