# Simple Data Analysis Example

import pandas as pd

# Load processed data
df = pd.read_csv('../datasets/processed_data.csv')

# Calculate basic statistics
summary = df.describe()

print("Data Analysis Summary:")
print(summary)
