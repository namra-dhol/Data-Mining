import pandas as pd

df = pd.DataFrame({'Age': [16, 20, 30, 40]})

# Min-Max
df['MinMax'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

# Z-Score
df['ZScore'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()

# Decimal Scaling
df['Decimal'] = df['Age'] / 100

print(df)