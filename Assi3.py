import pandas as pd
import numpy as np
from scipy import stats

# 1. Load COVID-19 dataset
df = pd.read_csv('C:\Users\sai\Desktop\FDSL\covid_19.csv')

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset information
print("\nDataset Description:")
print(df.describe())

# Display column names
print("\nColumn Names:")
print(df.columns)

# 2. Check the available columns
# Replace 'Confirmed' with the actual numerical column in your dataset

mean_val = df['Confirmed'].mean()
median_val = df['Confirmed'].median()
mode_val = df['Confirmed'].mode()[0]

print("\nMean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)

# 3. Using NumPy / SciPy
confirmed_array = df['Confirmed'].dropna().to_numpy()

print("\nNumPy Mean:", np.mean(confirmed_array))
print("NumPy Median:", np.median(confirmed_array))
print("SciPy Mode:", stats.mode(confirmed_array, keepdims=True))

# 4. Skewness
skewness = df['Confirmed'].skew()

print("\nSkewness:", skewness)

if mean_val > median_val:
    print("Distribution is right (positively) skewed")
elif mean_val < median_val:
    print("Distribution is left (negatively) skewed")
else:
    print("Distribution is approximately symmetric")