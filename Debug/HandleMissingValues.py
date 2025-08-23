import pandas as pd
df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [22, 25, None, 30]
})

# Fill with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df['Age'])
