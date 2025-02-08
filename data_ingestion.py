import requests
import sqlite3
import pandas as pd

DB_FILE = "weather.db"

API_KEY = '527f115550e8496c93482706250802'

def fetch_weather_data(api_url):
    """Fetches weather data from an API."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def save_to_db(data):
    """Saves weather data to SQLite."""
    conn = sqlite3.connect(DB_FILE)
    # df = pd.DataFrame(data)  # Convert JSON to DataFrame
    df = pd.json_normalize(data)
    df.to_sql("weather", conn, if_exists="replace", index=False)
    print(df.head())
    conn.close()

if __name__ == "__main__":
    API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=New York"
    weather_data = fetch_weather_data(API_URL)
    save_to_db(weather_data)
