import sqlite3
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
from geopy.geocoders import Nominatim

DB_FILE = "weather.db"

def load_data():
    """Loads weather data from SQLite."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM weather", conn)
    conn.close()
    return df

def get_lat_lon(city):
    """Fetches latitude and longitude for a given city."""
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None

def plot_animated_weather_map(df):
    """Plots an animated city-wise weather map using Folium."""
    
    # Base map
    weather_map = folium.Map(location=[20, 0], zoom_start=2)

    features = []
    
    for _, row in df.iterrows():
        lat, lon = get_lat_lon(row["city"])
        if lat and lon:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat],
                },
                "properties": {
                    "time": row["last_updated"],  # Animation timestamp
                    "popup": f"{row['city']}, {row['country']}<br>Temp: {row['temp_c']}°C<br>Humidity: {row['humidity']}%",
                    "icon": "cloud"
                }
            })

    # Add animated markers
    TimestampedGeoJson(
        {"type": "FeatureCollection", "features": features},
        period="PT1H",  # Animation step (hourly data)
        add_last_point=True,
    ).add_to(weather_map)

    # Save animated map
    weather_map.save("weather_map.html")
    print("✅ Animated Weather Map saved as 'weather_map.html'.")

if __name__ == "__main__":
    df = load_data()
    plot_animated_weather_map(df)
