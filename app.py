
import streamlit as st
from weather_download_function import generate_hdd

st.set_page_config(
    page_title="Heating Degree Day Generator",
    page_icon="🌡️",
)

st.title("Heating Degree Day Generator")

st.write(
"""
Generate a CSV containing Heating Degree Days
for all weather stations listed in weather_stations.csv.
"""
)

if st.button("Generate Dataset"):

    with st.spinner("Downloading weather data..."):

        weather = generate_hdd()

    st.success("Finished!")

    st.write(weather)

    csv = weather.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download HDD Dataset",
        data=csv,
        file_name="HDD65_by_location.csv",
        mime="text/csv",
    )