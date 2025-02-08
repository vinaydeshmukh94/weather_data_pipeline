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
    """Flattens JSON, removes duplicates, and saves weather data to SQLite."""
    conn = sqlite3.connect(DB_FILE)

    # Create table if not exists
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            country TEXT,
            temp_c REAL,
            humidity INTEGER,
            wind_kph REAL,
            last_updated TEXT,
            PRIMARY KEY (city, last_updated)  -- Prevent duplicates
        )
    """)
    conn.commit()

    # Extract only necessary fields
    records = []
    for item in data:
        if "current" in item and "location" in item:
            records.append({
                "city": item["location"]["name"],
                "country": item["location"]["country"],
                "temp_c": item["current"].get("temp_c", None),
                "humidity": item["current"].get("humidity", None),
                "wind_kph": item["current"].get("wind_kph", None),
                "last_updated": item["current"].get("last_updated", None)
            })

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Remove duplicates within the DataFrame before inserting
    df.drop_duplicates(subset=["city", "last_updated"], keep="last", inplace=True)

    # Insert into SQLite (duplicates will be ignored due to PRIMARY KEY)
    if not df.empty:
        df.to_sql("weather", conn, if_exists="replace", index=False)

    conn.close()


def fetch_and_save_data():
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
    
if __name__ == "__main__":
    fetch_and_save_data()
