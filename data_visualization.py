import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_data

def plot_temperature():
    df = load_data()
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=df["last_updated"], y=df["temp_c"], marker="o")
    
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends")
    plt.xticks(rotation=45)
    
    plt.show()

if __name__ == "__main__":
    plot_temperature()
