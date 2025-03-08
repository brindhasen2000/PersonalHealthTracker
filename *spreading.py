import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
import time

# Load dataset
file_path = "data/human_vitals_with_location.csv"
df = pd.read_csv(file_path)

# Define normal health metric ranges
NORMAL_RANGES = {
    "Heart Rate": (60, 100),
    "Respiratory Rate": (12, 20),
    "Body Temperature": (36.1, 37.2),
    "Oxygen Saturation": (95, 100),
    "Systolic Blood Pressure": (90, 120),
    "Diastolic Blood Pressure": (60, 80),
}

# Function to classify health status
def is_abnormal(row):
    for metric, (low, high) in NORMAL_RANGES.items():
        if metric in row and (row[metric] < low or row[metric] > high):
            return True
    return False

df['Status'] = df.apply(is_abnormal, axis=1)

# Initialize map
start_location = [df["Latitude"].mean(), df["Longitude"].mean()] # calculates central location by taking mean of all patient latitude/longitude. inital center point of map
health_map = folium.Map(location=start_location, zoom_start=5)
marker_cluster = MarkerCluster().add_to(health_map) # group nearby markers together to not overcrowd on the map

# Add patient nodes to map
def add_markers():
    for _, row in df.iterrows():
        color = "red" if row['Status'] else "green"
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"Patient ID: {row['Patient ID']}\nStatus: {'Abnormal' if row['Status'] else 'Normal'}"
        ).add_to(marker_cluster)

add_markers()

# Mapping
health_map.save("health_simulation.html")
print("Map has been saved as health_simulation.html. Open it in a browser.")
