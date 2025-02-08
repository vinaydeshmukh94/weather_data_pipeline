import sqlite3
import pandas as pd

DB_FILE = "weather.db"

def load_data():
    """Loads weather data from SQLite."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM weather", conn)
    conn.close()
    return df

def clean_data(df):
    """Performs data cleaning operations."""
    df.dropna(inplace=True)
    df["temp_c"] = df["temp_c"].astype(float)
    return df

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    print(df.head())
