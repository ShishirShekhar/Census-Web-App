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
            st.subheader("Distribution for Income groups")

            x1 = df["income"].value_counts()
            labels1 = x1.index
            fig1 = plt.figure(figsize=(12, 5))
            plt.pie(x=x1, labels=labels1, explode=[0, 0.2])
            st.pyplot(fig1)

            st.subheader("Distribution for Gender")

            x2 = df["gender"].value_counts()
            labels2 = x2.index
            fig2 = plt.figure(figsize=(12, 5))
            plt.pie(x=x2, labels=labels2, explode=[0, 0.2])
            st.pyplot(fig2)

        if (plots == "Box Plot"):
            st.subheader(plots)
            st.subheader("Box Plot for hours-per-week")

            fig1 = plt.figure(figsize=(12, 5))
            sns.boxplot(x="hours-per-week", y="gender", data=df)
            st.pyplot(fig1)

            fig2 = plt.figure(figsize=(12, 5))
            sns.boxplot(x="hours-per-week", y="income", data=df)
            st.pyplot(fig2)

        if (plots == "Count Plot"):
            st.subheader(plots)
            st.subheader("Count Plot for workclass")

            fig = plt.figure(figsize=(12, 5))
            sns.countplot(df["workclass"])
            st.pyplot(fig)