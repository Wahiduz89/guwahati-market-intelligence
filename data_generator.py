import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# CONFIGURATION
locations = ['Zoo Road', 'Anil Nagar', 'Jalukbari', 'Ganeshguri', 'Fancy Bazar']
flood_risk_zones = ['Anil Nagar', 'Zoo Road'] # High risk zones
start_date = datetime(2024, 1, 1)
num_transactions = 2500

# GENERATE DATES
date_list = [start_date + timedelta(days=x) for x in range(365)]
dates = [random.choice(date_list) for _ in range(num_transactions)]

# CREATE DATAFRAME
df = pd.DataFrame({
    'Transaction_ID': range(1, num_transactions + 1),
    'Date': dates,
    'Location': [random.choice(locations) for _ in range(num_transactions)],
    'Product_Category': [random.choice(['Electronics', 'Fashion', 'Home Essentials']) for _ in range(num_transactions)],
    'Base_Revenue': np.random.randint(500, 5000, size=num_transactions)
})

# APPLY FLOOD LOGIC (Resume Point: 40% drop in monsoon)
# Monsoon months: June (6), July (7), August (8)
def apply_flood_impact(row):
    month = row['Date'].month
    if row['Location'] in flood_risk_zones and month in [6, 7, 8]:
        # Simulate 40% revenue drop due to waterlogging
        return row['Base_Revenue'] * 0.60
    return row['Base_Revenue']

df['Final_Revenue'] = df.apply(apply_flood_impact, axis=1)

# SAVE TO CSV
print("Generating synthetic retail data for Guwahati...")
df.to_csv('guwahati_retail_data.csv', index=False)
print("Success! Dataset created with flood logic applied.")
