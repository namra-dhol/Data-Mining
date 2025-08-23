# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import pandas as pd
#
#
# df = pd.DataFrame({
#     'Math': [90, 80, 70, 60],
#     'Physics': [95, 85, 75, 65],
#     'Chemistry': [85, 75, 65, 55]
# })
#
# scaled = StandardScaler().fit_transform(df)
#
# pca = PCA(n_components=2)
# components = pca.fit_transform(scaled)
#
# print(pd.DataFrame(components, columns=['PC1', 'PC2']))

import pandas as pd
import numpy as np

# Step 1: Dataset
df = pd.DataFrame({
    'Math': [90, 80, 70, 60],
    'Physics': [95, 85, 75, 65],
    'Chemistry': [85, 75, 65, 55]
})

print("Original Data:")
print(df)

# Step 2: Standardize (mean = 0, std = 1)
X = df.values
X_meaned = X - np.mean(X, axis=0)
X_std = X_meaned / np.std(X_meaned, axis=0)

print("\nStandardized Data:")
print(X_std)

# Step 3: Covariance matrix
cov_matrix = np.cov(X_std.T)   # transpose so features are in rows
print("\nCovariance Matrix:")
print(cov_matrix)

# Step 4: Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Step 5: Sort eigenvectors by eigenvalues (descending)
idxs = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idxs]
eigenvectors = eigenvectors[:, idxs]

# Step 6: Select top k eigenvectors (say 2 PCs)
k = 2
eigenvectors_subset = eigenvectors[:, :k]

# Step 7: Transform data (Projection)
X_reduced = np.dot(X_std, eigenvectors_subset)

print("\nProjected Data (PC1, PC2):")
print(X_reduced)


# 🔹 What this does:
#1)  Standardize → Each feature (Math, Physics, Chemistry) gets mean=0, std=1.
#
# 2) Covariance matrix → Measures correlation between subjects.
#
#3)  Eigen decomposition → Finds principal components.
#
# 4) Sort eigenvectors → Keep directions with highest variance.
#
# 5) Project data → Multiply original data by top eigenvectors → new features PC1, PC2.
#

