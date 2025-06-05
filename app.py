import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Manesar Environment Dashboard", layout="wide")
st.title(" Environmental Analysis of Manesar, Gurgaon")
st.markdown("This dashboard presents real-world environmental insights from 8 datasets using interactive visualizations.")

@st.cache_data
def load_data():
    climate = pd.read_csv("data/manesar_climate_conditions.csv", encoding='ISO-8859-1')
    pollution = pd.read_csv("data/manesar_pollution_environment.csv", encoding='ISO-8859-1')
    land = pd.read_csv("data/manesar_land_use_urbanization.csv", encoding='ISO-8859-1')
    water = pd.read_csv("data/manesar_water_resources.csv", encoding='ISO-8859-1')
    forest = pd.read_csv("data/manesar_forest_biodiversity.csv", encoding='ISO-8859-1')
    geo = pd.read_csv("data/manesar_geological_topographical.csv", encoding='ISO-8859-1')
    disaster = pd.read_csv("data/manesar_disaster_risk.csv", encoding='ISO-8859-1')
    socio = pd.read_csv("data/manesar_socio_economic_real.csv", encoding='ISO-8859-1')

    for df in [climate, pollution, land, water, forest, geo, disaster, socio]:
        df.columns = df.columns.str.strip().str.replace('\u200b', '', regex=False)

    climate['Year'] = pd.to_numeric(climate['Year'], errors='coerce')
    pollution['Year'] = pd.to_numeric(pollution['Year'], errors='coerce')
    land['Year'] = pd.to_numeric(land['Year'], errors='coerce')

    return climate, pollution, land, water, forest, geo, disaster, socio

climate, pollution, land, water, forest, geo, disaster, socio = load_data()
with st.expander(" Climate Trends"):
    min_year = int(climate['Year'].min())
    max_year = int(climate['Year'].max())
    selected_year = st.slider("Select Year (Climate)", min_year, max_year, min_year)
    climate_filtered = climate[climate['Year'] == selected_year]

    temp_col = next((c for c in climate.columns if "temp" in c.lower()), None)
    if not climate_filtered.empty and temp_col:
        fig, ax = plt.subplots()
        sns.lineplot(data=climate_filtered, x='Month', y=temp_col, marker='o', ax=ax)
        ax.set_title(f"Average Temperature in {selected_year}")
        st.pyplot(fig)
    else:
        st.warning("No temperature data available.")

with st.expander(" Pollution Levels"):
    fig2, ax2 = plt.subplots()
    sns.barplot(data=pollution, x='Year', y='Avg PM2.5 (µg/m³)', color='orange', ax=ax2)
    ax2.set_title("PM2.5 Trend Over Years")
    st.pyplot(fig2)

with st.expander(" Land Use Changes"):
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=land, x='Year', y='Built-up Area (sq km)', label='Built-up', ax=ax3)
    sns.lineplot(data=land, x='Year', y='Agricultural Land (sq km)', label='Agriculture', ax=ax3)
    sns.lineplot(data=land, x='Year', y='Green/Open Spaces (sq km)', label='Open Spaces', ax=ax3)
    ax3.set_title("Land Use Over Time")
    ax3.legend()
    st.pyplot(fig3)
with st.expander(" Water Resources Overview"):
    fig4, ax4 = plt.subplots()
    sns.lineplot(data=water, x='Year', y='Groundwater Level (m below ground)', marker='o', label='Groundwater', ax=ax4)
    sns.lineplot(data=water, x='Year', y='Water Quality Index (0-100)', marker='o', label='WQI', ax=ax4)
    ax4.set_title("Water Quality & Groundwater Trends")
    ax4.legend()
    st.pyplot(fig4)

with st.expander(" Forest & Biodiversity"):
    fig5, ax5 = plt.subplots()
    sns.barplot(data=forest, x='Year', y='Recorded Forest Area (sq km)', color='green', ax=ax5)
    ax5.set_title("Forest Area Over Time")
    st.pyplot(fig5)

    fig5b, ax5b = plt.subplots()
    sns.lineplot(data=forest, x='Year', y='Tree Cover Loss (ha)', marker='o', color='red', ax=ax5b)
    ax5b.set_title("Tree Cover Loss Over Time")
    st.pyplot(fig5b)

with st.expander(" Geological & Topographical Data"):
    fig6, ax6 = plt.subplots()
    sns.countplot(data=geo, x='Soil Type', palette='viridis', ax=ax6)
    ax6.set_title("Soil Type Distribution in Manesar")
    st.pyplot(fig6)

with st.expander(" Disaster Risk Factors"):
    fig7, ax7 = plt.subplots()
    sns.barplot(data=disaster, x='Risk Type', y='Severity (Scale 1-5)', palette='flare', ax=ax7)
    ax7.set_title("Disaster Risk Severity by Type")
    st.pyplot(fig7)

with st.expander("👥 Socio-Economic Overview"):
    st.markdown("Overview of current socio-economic statistics for Manesar:")

    # Show as table
    st.dataframe(socio)

# Final Footer
st.markdown("---")
st.markdown(" **by Ashish Sahu** ") 
st.markdown("Made with  using Streamlit | [GitHub Repo](https://github.com/Ashish-s2/manesar-environment-analysis)")

