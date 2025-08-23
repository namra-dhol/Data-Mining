import pandas as pd

# Scores of students
data = {'Score': [23, 45, 67, 89, 90, 95, 100, 55, 60]}
df = pd.DataFrame(data)

# Equal-width binning into 3 bins
df['Equal_Width_Bin'] = pd.cut(df['Score'], bins=3, labels=["Low", "Medium", "High"])
# df['Equal_Width_Bin'] = pd.cut(df['Score'], bins=3)

print(df)


# Equal-frequency binning into 3 bins
df['Equal_Freq_Bin'] = pd.qcut(df['Score'], q=3, labels=["Low", "Medium", "High"])
print(df)

print(df)


