# Import necessary modules
import streamlit as st
from preprocessing import load_data
from web_functions import visualize, view_data

# Config streamlit page
st.set_page_config(
    page_title="Census Visualisation Web App",
    page_icon="chart_with_upwards_trend",
    layout="centered",
    initial_sidebar_state="auto"
)

# Code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)

# Add title on the main page and in the sidebar.
st.title("Census Visualisation Web App")

# Add app description
st.text("This web app allows a user to explore and visualize census data")

# Add a subheader to view data
st.header("View Data")

# Load the data
df = load_data()

# View Dataset Configuration
view_data(df)

# Add a subheader in the sidebar with the label "Visualisation Selector"
st.header("Visualization Selector")

# Add a multiselect widget to allow the user to select multiple visualisations.
plot_list = st.multiselect("Select the Charts/Plots:", ["Pie Plot", "Box Plot", "Count Plot"])

# Call visualize call to get the desired plots
visualize(df, plot_list)