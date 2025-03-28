import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Drop rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a map centered around the average location
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add restaurant locations as markers
marker_cluster = MarkerCluster().add_to(restaurant_map)

for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Restaurant Name']} - {row['City']}",
        icon=folium.Icon(color="blue", icon="cutlery", prefix="fa")
    ).add_to(marker_cluster)

# Save map as HTML file
restaurant_map.save("restaurant_map.html")

print("Map has been generated and saved as 'restaurant_map.html'. Open it in a browser to view.")
