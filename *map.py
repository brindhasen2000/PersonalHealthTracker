#Works

import folium
import pandas as pd
import math

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

file_path = "data/human_vitals_with_location.csv"  # Add path to your dataset
df = pd.read_csv(file_path)
locations = []

locations = [ (37.7749, -122.4194), (38.7749, -121.4194) ]
m = folium.Map(location=locations[0], zoom_start=5)

prelat = 37.7749
prelon = -122.4194
for index, row in df.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']

    distance = haversine(lat, lon, prelat, prelon)
    print(f"The distance between the two points is {distance:.2f} kilometers.")

    prelat = lat
    prelon = lon
    
    # Create a map centered around the first location
    folium.Marker([lat, lon], popup=f"Lat: {lat}, Lon: {lon}").add_to(m)


# Save map to an HTML file
m.save("map.html")
print("done!!")


