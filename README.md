
# Weather Data Pipeline with Animated Map

## 📌 Project Overview

This project fetches real-time weather data from an API, stores it in an SQLite database, and visualizes it on an interactive, animated map using Folium.

## 🚀 Features

Fetches live weather data for multiple cities.

Stores data in SQLite with duplicate prevention.

Processes and cleans data before visualization.

Interactive & Animated Weather Map using Folium.

Displays city-wise temperature, humidity, and wind speed.

## 📦 Installation

🔹 Step 1: Clone the Repository

```
git clone https://github.com/vindeshmukh94/weather-data-pipeline.git
cd weather-data-pipeline
```
🔹 Step 2: Install Dependencies

```pip install -r requirements.txt```

Required packages: requests, pandas, sqlite3, folium, geopy

## ⚙️ How It Works

1️⃣ Fetch Weather Data

The script fetches weather data from WeatherAPI.

Stores data in SQLite with a primary key to avoid duplicates.

Runs a loop to collect data for multiple cities.

2️⃣ Process & Clean Data

Converts JSON response to a structured Pandas DataFrame.

Checks for missing values and removes duplicates.

3️⃣ Generate Animated Map

Uses Folium + Leaflet's TimestampedGeoJson to animate markers over time.

Each marker displays City, Temperature, Humidity, and Wind Speed.

Saves an interactive animated_weather_map.html file.

## 🚀 Usage

🔹 Step 1: Set Up API Key

Sign up at WeatherAPI and get your API key.

Add your API key in data_ingestion.py:

```API_KEY = "your_api_key_here"```

🔹 Step 2: Run the Pipeline

Fetch weather data and store it in the database:

```python data_ingestion.py```

🔹 Step 3: Process & Visualize Data

Generate the animated weather map:

```python data_processing.py```

🔹 Step 4: View the Map

Open the weather_map.html file in your browser.

Watch the animated city-wise weather updates. 🌍⏳

🛠️ Project Structure
```
weather_data_pipeline/
│-- data_ingestion.py   # Fetches & stores weather data
│-- data_processing.py  # Cleans data & generates an animated map
│-- weather.db          # SQLite database storing weather data
│-- animated_weather_map.html  # Generated weather map
│-- README.md           # Project documentation
```
