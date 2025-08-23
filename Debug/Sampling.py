import pandas as pd

df = pd.DataFrame({'ID': range(1, 101)})

# Simple random sample (without replacement)
sampled = df.sample(n=10, random_state=1)
print(sampled)

# With replacement
sampled_wr = df.sample(n=10, replace=True, random_state=1)
print(sampled_wr)