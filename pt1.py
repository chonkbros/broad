import requests
import pandas as pd

# API endpoint
url = "https://api-v3.mbta.com/routes"

# Query parameters
params = {
    "filter[type]": "0,1"
}

# Make the GET request
response_1 = requests.get(url, params=params)


response_1 = response_1.json()


df = pd.DataFrame(response_1['data'])
df_attributes = df['attributes'].apply(pd.Series)
names = df_attributes['long_name']

print(names)