"""This module creates the visulisation page"""

# Import necessary modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def app(df):
    """This function creates the visulisation page"""
    # Add a subheader in the sidebar with the label "Visualisation Selector"
    st.header("Visualization Selector")

    # Add a multiselect widget to allow the user to select multiple visualisations.
    plot_list = st.multiselect("Select the Charts/Plots:", ["Pie Plot", "Box Plot", "Count Plot"])

    # Using the 'if' statement, display raw data on the click of the checkbox.
    for plots in plot_list:
        if (plots == "Pie Plot"):
            st.subheader(plots)
            pie_col = st.multiselect("Select column", ["income", "gender"])

            for col in pie_col:
                st.subheader(f"Distribution for {col}")

                x = df[col].value_counts()
                labels = x.index
                fig = plt.figure(figsize=(12, 5))
                plt.pie(x=x, labels=labels, explode=[0, 0.2], autopct='%.1f%%')
                st.pyplot(fig)

        if (plots == "Box Plot"):
            st.subheader(plots)
            box_col = st.multiselect("Select hours-per-week vs column", ["income", "gender"])
            
            st.subheader("Box Plot for hours-per-week")
            for col in box_col:
                fig = plt.figure(figsize=(12, 5))
                sns.boxplot(x="hours-per-week", y="gender", data=df)
                st.pyplot(fig)

        if (plots == "Count Plot"):
            st.subheader(plots)
            st.subheader("Count Plot for workclass")

            fig = plt.figure(figsize=(12, 5))
            sns.countplot(df["workclass"])
            st.pyplot(fig)