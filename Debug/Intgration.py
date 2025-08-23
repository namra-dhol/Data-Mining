import  pandas as pd

df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['A', 'B']})
print(df1)

df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 85]})
print(df2)

merged = pd.merge(df1, df2, on='ID')

print(merged)