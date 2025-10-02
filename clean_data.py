import pandas as pd
import numpy as np
import re

# Function to validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Read the CSV with tab separator
df = pd.read_csv("customers.csv", sep="\t")

print("Columns in CSV:", df.columns.tolist())
print(df.head())

# Clean email column
if 'email' in df.columns:
    df['email'] = df['email'].apply(lambda x: x if is_valid_email(str(x)) else np.nan)
else:
    print("⚠️ Warning: 'email' column not found in CSV, skipping email cleaning")

# Clean age column (age > 0)
if 'age' in df.columns:
    df['age'] = df['age'].apply(lambda x: x if pd.notnull(x) and x > 0 else np.nan)
else:
    print("⚠️ Warning: 'age' column not found in CSV, skipping age cleaning")

# Save cleaned data
df.to_csv("customers_cleaned.csv", index=False)

print("✅ Data cleaning completed. Cleaned data saved to 'customers_cleaned.csv'.")
