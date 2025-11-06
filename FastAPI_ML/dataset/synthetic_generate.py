import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# Define possible categories
cities_tier1 = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
cities_tier2 = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]
all_cities = cities_tier1 + cities_tier2

occupations = [
    "retired", "freelancer", "student",
    "government_job", "business_owner",
    "unemployed", "private_job"
]

premium_categories = ["Low", "Medium", "High"]

# Generate 100 synthetic rows
n = 100
data = {
    "age": np.random.randint(18, 70, n),
    "weight": np.random.normal(70, 15, n).round(1),
    "height": np.random.normal(1.65, 0.1, n).round(2),
    "income_lpa": np.random.uniform(1, 40, n).round(3),
    "smoker": np.random.choice([True, False], n, p=[0.3, 0.7]),
    "city": np.random.choice(all_cities, n),
    "occupation": np.random.choice(occupations, n),
}

df = pd.DataFrame(data)

# Basic rule-based target creation (so model learns something meaningful)
def get_premium_category(row):
    bmi = row["weight"] / (row["height"] ** 2)
    if row["smoker"] and (bmi > 30 or row["income_lpa"] > 20):
        return "High"
    elif row["income_lpa"] < 8:
        return "Medium"
    else:
        return np.random.choice(["Low", "Medium"], p=[0.6, 0.4])

df["insurance_premium_category"] = df.apply(get_premium_category, axis=1)

# Save to CSV
df.to_csv("./x_fastapi&ml/dataset/insurance.csv", index=False)

print(df.sample(5))