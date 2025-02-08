from data_ingestion import fetch_and_save_data
from data_processing import load_data, plot_animated_weather_map

def main():
    """Runs the full weather data pipeline."""
    print("Fetching data...")
    fetch_and_save_data()
    
    print("Processing data...")
    df = load_data()
    
    print("Visualizing data...")
    plot_animated_weather_map(df)

if __name__ == "__main__":
    main()
