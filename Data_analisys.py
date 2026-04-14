import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

# Basic save (includes index by default)
df.to_csv('output.csv')

# Common standard save (removes index)
df.to_csv('output.csv', index=False)