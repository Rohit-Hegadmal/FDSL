import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

df = pd.read_csv("Clinic.csv")
print(df.head())
print(df.describe())
print(df.info())
successes = df['Outcome'].sum()
trials = len(df['Outcome'])
p = successes / trials

n = trials
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

mean, var = binom.stats(n, p, moments='mv')
std_dev = np.sqrt(var)

print('Mean (Expected successes):', mean)
print('Variance:', var)
print('Standard Deviation:', std_dev)

plt.figure(figsize=(8, 5))
plt.bar(x, pmf, color='skyblue', edgecolor='black', label='PMF')
plt.axvline(mean, color='red', linestyle='--', label='Mean')
plt.title(f'Binomial Distribution (n={n}, p={p:.2f})')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.legend()
plt.show()

p_at_least_5 = 1 - binom.cdf(4, n, p)
print('P(X >= 5):', p_at_least_5)

p_exactly_8 = binom.pmf(8, n, p)
print('P(X = 8):', p_exactly_8)
