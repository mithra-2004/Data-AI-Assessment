import requests
import pandas as pd

# API endpoint
url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

# Fetch data from API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract current weather data
current_weather = data["current_weather"]

# Convert to DataFrame
weather_df = pd.DataFrame([current_weather])

# Save as CSV
weather_df.to_csv("weather_data.csv", index=False)

print("Weather data fetched and saved successfully")
