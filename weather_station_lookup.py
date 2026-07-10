


## this script pulls the appropriate meteostat weather stations to be used in the app script

## pull in packages
from datetime import datetime, timedelta
from meteostat import daily, Point
import pandas as pd
from meteostat import stations

## list of locations
locations = {
    "Antigo": (45.1403, -89.1523),
    "Appleton": (44.2619, -88.4154),
    "Ashland": (46.5924, -90.8838),
    "Cambridge, MN": (45.5727, -93.2244),
    "Decorah, IA": (43.3033, -91.7857),
    "Dubuque, IA": (42.5006, -90.6646),
    "Duluth": (46.7867, -92.1005),
    "Eau Claire": (44.8113, -91.4985),
    "Green Bay": (44.5133, -88.0133),
    "Iron Mountain": (45.8202, -88.0650),
    "Ironwood": (46.4547, -90.1710),
    "Janesville": (42.6828, -89.0187),
    "La Crosse": (43.8014, -91.2396),
    "Lone Rock": (43.1836, -90.1907),
    "Madison": (43.0731, -89.4012),
    "Manitowoc": (44.0886, -87.6576),
    "Marinette": (45.0999, -87.6307),
    "Marshfield": (44.6689, -90.1718),
    "Milwaukee": (43.0389, -87.9065),
    "Mosinee": (44.7930, -89.7035),
    "Oshkosh": (44.0247, -88.5426),
    "Phillips": (45.6955, -90.4015),
    "Red Wing, MN": (44.5625, -92.5338),
    "Rhinelander": (45.6366, -89.4121),
    "Rice Lake": (45.5061, -91.7382),
    "Sturgeon Bay": (44.8342, -87.3770),
    "Watertown": (43.1947, -88.7281),
    "Wausau": (44.9591, -89.6301),
    "Winona, MN": (44.0499, -91.6393),
    "Woodruff": (45.9047, -89.7035)
}

results = []

for name, (lat, lon) in locations.items():
    point = Point(lat, lon)

    nearby = stations.nearby(point)

    # closest station
    station_df = nearby.head(1).copy()

    # convert index (station ID) into a column
    station_df = station_df.reset_index()

    # rename for clarity
    station_df = station_df.rename(columns={"id": "station_id"})

    station_df["location"] = name

    results.append(station_df)

station_lookup = pd.concat(results, ignore_index=True)

print(station_lookup[["location", "station_id", "name"]])

station_lookup = station_lookup[["location", "station_id"]]


## save csv of the weather stations

station_lookup.to_csv("weather_stations.csv", index=False)

