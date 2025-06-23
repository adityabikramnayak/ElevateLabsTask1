# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Loading the dataset
df = pd.read_csv("C://Users//KIIT//OneDrive//Desktop//ELAB//Titanic-Dataset.csv")

# Basic info
print(df.head())
print(df.info())
print(df.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Handling missing values

# Filling missing values in 'Age' column with the median
age_median = df['Age'].median()
for i in range(len(df)):
    if pd.isnull(df.loc[i, 'Age']):
        df.loc[i, 'Age'] = age_median

# Filling missing values in 'Embarked' column with the mode
embarked_mode = df['Embarked'].mode()[0]
for i in range(len(df)):
    if pd.isnull(df.loc[i, 'Embarked']):
        df.loc[i, 'Embarked'] = embarked_mode

# Droping the 'Cabin' column because it has too many missing values
df.drop('Cabin', axis=1, inplace=True)

# 3. Converting categorical columns to numeric 

# Converting 'Sex' column: male = 1, female = 0
for i in range(len(df)):
    if df.loc[i, 'Sex'] == 'male':
        df.loc[i, 'Sex'] = 1
    else:
        df.loc[i, 'Sex'] = 0

# Converting 'Embarked' into two new columns: 'Embarked_Q' and 'Embarked_S'
df['Embarked_Q'] = 0
df['Embarked_S'] = 0

for i in range(len(df)):
    if df.loc[i, 'Embarked'] == 'Q':
        df.loc[i, 'Embarked_Q'] = 1
    elif df.loc[i, 'Embarked'] == 'S':
        df.loc[i, 'Embarked_S'] = 1

# Droping the original 'Embarked' column
df.drop('Embarked', axis=1, inplace=True)

# 4. Standardizing 'Age' and 'Fare'  (Z = (X - mean) / std)

# Standardized 'Age'
age_mean = df['Age'].mean()
age_std = df['Age'].std()

for i in range(len(df)):
    df.loc[i, 'Age'] = (df.loc[i, 'Age'] - age_mean) / age_std

# Standardized 'Fare'
fare_mean = df['Fare'].mean()
fare_std = df['Fare'].std()

for i in range(len(df)):
    df.loc[i, 'Fare'] = (df.loc[i, 'Fare'] - fare_mean) / fare_std

# 5. Showing final result
print("Done! Here's the cleaned data:")
print(df.head())

# Checked for any remaining missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Boxplot to visualize outliers in 'Age' and 'Fare'
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x=df['Age'])
plt.title('Boxplot of Standardized Age')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Fare'])
plt.title('Boxplot of Standardized Fare')

plt.tight_layout()
plt.show()

# Saving the cleaned data File
df.to_csv("C:\\Users\\KIIT\\OneDrive\\Desktop\\ELAB\\cleaned_titanic.csv", index=False)








