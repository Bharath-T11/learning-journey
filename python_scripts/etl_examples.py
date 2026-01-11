# Simple ETL example: Read CSV, process data, save to new CSV

import pandas as pd

# Load sample dataset
df = pd.read_csv('../datasets/sample_data.csv')

# Simple transformation
df['Total'] = df['Quantity'] * df['Price']

# Save processed data
df.to_csv('../datasets/processed_data.csv', index=False)

print("ETL process completed! Processed data saved to processed_data.csv")
