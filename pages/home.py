"""This module creates the home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function creates the home page"""
    # Add title on the main page and in the sidebar.
    st.title("Census Visualisation Web App")

    # Add image
    with st.columns([1, 6, 1])[1]:
        st.image("./images/visualization.png")

    # Add app description
    st.text("This web app allows a user to explore and visualize census data")