import pandas as pd 
import numpy as np

a=[10,20,30,40,50,34,23,45,67,89]

a_range = max(a) - min(a)
print("Range of the data is:", a_range)

print("\n")

a_variance = np.var(a)
print("Variance of the data is:", a_variance)

a_std_dev = np.std(a)
print("Standard Deviation of the data is:", a_std_dev)

a_coeff_var = a_std_dev / np.mean(a)
print("Coefficient of Variation of the data is:", a_coeff_var)

a_interquartile_range = np.percentile(a, 75) - np.percentile(a, 25)
print("Interquartile Range of the data is:", a_interquartile_range)

#without using functions

print("\n")


a_mean = sum(a) / len(a)
print("Mean of the data is:", a_mean)
