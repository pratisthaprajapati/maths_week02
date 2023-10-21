import datetime
print(datetime.datetime.today())
import numpy as np
import matplotlib.pyplot as plt

# Given data
X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
Y = np.array([30, 25, 95, 115, 265, 325, 570, 700, 1085, 1300])

# Calculate the coefficients 𝑏1 (slope) and 𝑏0 (intercept)
n = len(X)
mean_x = np.mean(X)
mean_y = np.mean(Y)
b1 = np.sum((X - mean_x) * (Y - mean_y)) / np.sum((X - mean_x) ** 2)
b0 = mean_y - b1 * mean_x

# Calculate the coefficient of linear correlation (r)
r = np.corrcoef(X, Y)[0, 1]

# Print the calculated values
print(f"Slope 𝑏1: {b1}")
print(f"Intercept 𝑏0: {b0}")
print(f"Coefficient of linear correlation r: {r}")

# Plot the dataset and the linear regression line
plt.scatter(X, Y, label="Data Points")
plt.plot(X, b0 + b1 * X, color='red', label="Linear Regression Line")
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
