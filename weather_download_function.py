
from datetime import datetime, timedelta
from meteostat import daily
import pandas as pd


def generate_hdd():

    station_data = pd.read_csv("weather_stations.csv")

    end = datetime.now()
    start = end - timedelta(days=60)

    weather = None

    total = len(station_data)

    for i, (_, row) in enumerate(station_data.iterrows()):

        station_id = row["station_id"]
        location = row["location"]

        print(f"{i+1}/{total}: {location}")

        df = daily(station_id, start, end).fetch()

        if df.empty:
            continue

        tavg_f = df["temp"] * 9 / 5 + 32

        df[location] = (65 - tavg_f).clip(lower=0)

        df = df[[location]]

        if weather is None:
            weather = df
        else:
            weather = weather.join(df, how="outer")

    weather = weather.reset_index()

    weather = weather.rename(columns={"time": "date"})

    return weather