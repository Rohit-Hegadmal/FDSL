import numpy as np

num = np.array([1, 2, 2, 4, 5, 6])
num1 = np.array([1, 4, 8, 5, 9])

print(np.mean(num))
print(np.sum(num))
print(np.sqrt(num))
print(np.exp(num))

num2 = np.eye(2, 3)
print(num2)

num3 = np.ones((2, 3))
print(num3)

num4 = np.zeros((3, 4))
print(num4)

num5 = np.arange(1, 10, 2)
print(num5)

num6 = np.linspace(1, 10, 5)
print(num6)

num7 = np.random.rand(2, 4)
print(num7)

print(np.min(num))
print(np.max(num))
print(np.sort(num))

print(np.min(num1))
print(np.max(num1))
print(np.sort(num1))
print(np.sum(num1))
print(np.sqrt(num1))
print(np.exp(num1))