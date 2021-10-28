# Import necessary modules
import streamlit as st
from preprocessing import load_data
from pages import home, data, visualisation, about

# Config streamlit page
st.set_page_config(
    page_title = "Census Visualisation Web App",
    page_icon = "chart_with_upwards_trend",
    layout = "centered",
    initial_sidebar_state = "auto"
)

# Code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the data
df = load_data()

# Create dict for pages
pages = {
    "Home": home,
    "View Data": data,
    "Visualisation": visualisation,
    "About": about
}

# Create sidebar
st.sidebar.title("Navigation")

# Create radio to select the page
page = st.sidebar.radio("Pages", list(pages.keys()))


if page in ["View Data", "Visualisation"]:
    pages[page].app(df)
else:
    pages[page].app()
