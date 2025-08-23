import pandas as pd
df = pd.DataFrame({'Age': [10, 22, 23, 41, 50, 60, 70, 90, 100]})
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 22, 70, 100], labels=['Young', 'Mature', 'Senior'])

print(df)