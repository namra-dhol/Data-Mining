import pandas as pd
import numpy as np

# Create dataframe
df = pd.DataFrame({'Score': [50, 51, 52, 1000]})



# Step 1: calculate mean
mean = df['Score'].mean()

# Step 2: calculate standard deviation
std = df['Score'].std(ddof=0)  # population std, use ddof=1 for sample std

# Step 3: calculate z-score manually
df['z_score'] = (df['Score'] - mean) / std

# Step 4: detect outliers (|z| > 2)
outliers = df[df['z_score'].abs() > 2]

print("Full DataFrame:")
print(df)
print("\nOutliers:")
print(outliers)



