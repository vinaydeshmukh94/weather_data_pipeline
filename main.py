from data_ingestion import fetch_weather_data, save_to_db
from data_processing import load_data, clean_data
from data_visualization import plot_temperature

API_URL = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=New York"

def main():
    """Runs the full weather data pipeline."""
    print("Fetching data...")
    weather_data = fetch_weather_data(API_URL)
    
    print("Saving to database...")
    save_to_db(weather_data)
    
    print("Processing data...")
    df = load_data()
    df = clean_data(df)
    
    print("Visualizing data...")
    plot_temperature()

if __name__ == "__main__":
    main()
