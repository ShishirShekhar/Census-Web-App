"""This module creates the view data page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function creates the view data page"""
    # View Dataset Configuration
    
    # Add a subheader to view data
    st.header("View Data")

    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.dataframe(df)

    # Create three olumns.
    st.subheader("Columns Description:")
    cols = st.columns([1, 1, 1])

    # Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
    with cols[0]:
        if st.checkbox("Show all columns names"):
            st.dataframe(df.columns)

    # Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
    with cols[1]:
        if st.checkbox("View columns data-types"):
            st.dataframe(df.dtypes.apply(lambda x: x.name))

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with cols[2]:
        if st.checkbox("View columns data"):
            col = st.selectbox("Select column", list(df.columns))
            st.dataframe(df[col])

    # Display summary of the dataset on the click of checkbox.
    if st.checkbox("Show summary"):
        st.dataframe(df.describe())