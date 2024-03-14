import numpy as np
from scipy.linalg import svd
ratings_data = np.array([
    [5, 4, 0, 2, 1],
    [3, 2, 0, 4, 5],
    [0, 0, 5, 4, 3],
    [1, 2, 3, 0, 0]
])
U, sigma, VT = svd(ratings_data)
num_factors_to_keep = 2

# Choose the number of factors to keep
important_factors = VT[:num_factors_to_keep]

# Print the important factors
print("Important factors affecting ratings:")
for i, factor in enumerate(important_factors):
    print(f"Factor {i+1}: {factor}")

# Calculate the reconstructed ratings matrix using the important factors
reconstructed_ratings = np.dot(np.dot(U[:, :num_factors_to_keep], np.diag(sigma[:num_factors_to_keep])), VT[:num_factors_to_keep])

# Print the reconstructed ratings matrix
print("\nReconstructed ratings matrix:")
print(reconstructed_ratings)
