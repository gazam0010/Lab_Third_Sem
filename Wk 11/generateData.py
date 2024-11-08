import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate nominal data for customer demographics
gender = np.random.choice(['Male', 'Female'], size=100)  # nominal data
location = np.random.choice(['Urban', 'Suburban', 'Rural'], size=100)  # nominal data
age_group = np.random.choice(['18-25', '26-35', '36-45', '46-55', '56+'], size=100)  # nominal data

# Generate continuous data for spending habits
annual_income = np.random.normal(loc=60000, scale=15000, size=100)  # continuous (mean=60000, std=15000)
spending_score = np.random.normal(loc=50, scale=15, size=100)  # continuous (mean=50, std=15)
number_of_purchases = np.random.poisson(lam=5, size=100)  # count data for number of purchases

# Generate binary dependent variable 'purchase_made' based on spending habits
purchase_made = (spending_score + np.random.normal(0, 5, size=100) > 50).astype(int)  # binary

# Create the DataFrame
data = pd.DataFrame({
    'gender': gender,
    'location': location,
    'age_group': age_group,
    'annual_income': annual_income,
    'spending_score': spending_score,
    'number_of_purchases': number_of_purchases,
    'purchase_made': purchase_made
})

# Save to CSV for later use
data.to_csv('customer_behavior_data.csv', index=False)

print("Synthetic customer behavior data generated and saved to 'customer_behavior_data.csv'")
