import plotly.express as px
import pandas as pd
import re

class heatMapItemsFrequencies:
    def __init__(self, itemsFrequenciesDictionary):
        self.itemsFrequenciesDictionary = itemsFrequenciesDictionary

    def plotHeatMap(self):
        # Initialize lists to store latitude, longitude, and frequency values
        latitudes = []
        longitudes = []
        vals = []

        # Iterate through each coordinate-frequency pair in the itemsFrequenciesDictionary
        for coord, freq in self.itemsFrequenciesDictionary.items():
            try:
                # Extract latitude and longitude values from the coordinate using regex
                longitude, latitude = re.findall(r'\d+\.\d+', coord)
                latitudes.append(float(latitude))
                longitudes.append(float(longitude))
                vals.append(freq)
            except:
                # If there is an error in extraction, continue to the next pair
                continue

        # Create a pandas DataFrame to store the extracted data
        df = pd.DataFrame()
        df["latitude"] = latitudes
        df["longitude"] = longitudes
        df["val"] = vals

        # Create a heatmap using plotly express density_mapbox
        fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='val', radius=10, zoom=4)

        # Set the map style to "open-street-map" and adjust the layout margins
        fig.update_layout(mapbox_style="open-street-map", margin={"r":0, "t":0, "l":0, "b":0})

        # Display the generated heatmap
        fig.show()
