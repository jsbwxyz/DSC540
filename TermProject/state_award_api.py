import requests
import pandas as pd

# Define API URL
url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"

# Pull back everthing from USASpendingAPI
payload = {
    "filters": {
        "time_period": [{"start_date": "2024-10-01", "end_date": "2025-09-30"}],
        "place_of_performance_locations": [{"country": "USA"}], # Get all states
        "award_type_codes": ["A", "B", "C", "D"]
    },
    "fields": [
        "Award ID", 
        "Recipient Name", 
        "Total Obligation",
        "Place of Performance State Code",   # Shows 'TX', 'CA', etc.
        "Place of Performance State Name",   # Shows 'TEXAS'
        "Place of Performance County Code",  # Numeric County FIPS
        "Place of Performance Zip5",
        "Awarding Agency",
        "Awarding Sub Agency",
        "Contract Award Type",
        "Description",
        "naics_code",                        # Industry Code (Great for Retail)
        "naics_description",
        "period_of_performance_start_date",
        "recipient_id"
    ],
    "limit": 100, # Can be iterated up to 1000
    "page": 1
}

# Fetch Data
print("Connecting to USAspending API...")
response = requests.post(url, json=payload)

if response.status_code == 200:
    # Put into a dataframe called 
    raw_data = response.json()
    spending_df = pd.DataFrame(raw_data['results'])
    
    # 5. Export to CSV
    filename = "federal_spending_by_state.csv"
    spending_df.to_csv(filename, index=False)
    
    print(f"Success! Data saved to {filename}")
    print("\n--- Preview of Data with State Codes ---")
    print(spending_df[['Award ID', 'Recipient Name', 'Place of Performance State Code', 'Total Obligation']].head())
else:
    print(f"Failed. Error Code: {response.status_code}")