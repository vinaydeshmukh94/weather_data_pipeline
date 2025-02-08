import requests
import sqlite3
import pandas as pd
import time

DB_FILE = "weather.db"
API_KEY = "527f115550e8496c93482706250802"
LOCATIONS = [
    "New York", "London", "Tokyo", "Sydney", "Mumbai", "Paris", "Berlin", "Toronto",
    "Los Angeles", "Dubai", "Beijing", "Moscow", "São Paulo", "Cape Town", "Singapore"
]

def fetch_weather_data(location):
    """Fetches weather data for a given location."""
    API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {location}: {response.status_code}")
        return None

def save_to_db(data):
    """Flattens JSON and saves weather data to SQLite."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.json_normalize(data)
    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    all_weather_data = []

    for location in LOCATIONS:
        print(f"Fetching data for {location}...")
        data = fetch_weather_data(location)
        if data:
            all_weather_data.append(data)
        time.sleep(1)  # Avoid hitting API rate limits

    if all_weather_data:
        save_to_db(all_weather_data)
        print("✅ Weather data saved successfully!")
