import csv
import numpy as np

# Load CSV data
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    data = list(reader)

# Convert data to float and organize it in dictionaries
names = [row[0] for row in data]
clout = np.array([float(row[1]) for row in data])
salience = np.array([float(row[2]) for row in data])
position = np.array([float(row[3]) for row in data])

# Calculate the weights and the weighted sum
numerator = np.sum(clout * salience * position)
denominator = clout * salience

# Calculate the weighted mean
weighted_mean = numerator / np.sum(denominator)

# Subtract the weighted mean from each position to find the difference
difference = np.abs(position - weighted_mean)

# Find the index of the minimum difference
min_index = np.argmin(difference)

# Print the weighted mean, name of the individual, and their position
print(f"The weighted mean position is {weighted_mean:.2f}.")
print(f"The individual closest to the weighted mean is {names[min_index]} with a position of {position[min_index]:.2f}.")