# Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from preprocessing import load_data

# Load the data
census_df = load_data()

# Write your code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)

# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title("Adult Census")
# Using the 'if' statement, display raw data on the click of the checkbox.

# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.header("Visualization Selector")

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
ploy_list = st.multiselect("Select the Charts/Plots:", ["Pie Plot", "Box Plot", "Count Plot"])

for plots in ploy_list:
    # Display pie plot using matplotlib module and 'st.pyplot()'
    if (plots == "Pie Plot"):
        st.subheader("Distribution for Income groups")
        x1 = census_df["income"].value_counts()
        labels1 = x1.index
        fig1 = plt.figure(figsize=(12, 5))
        plt.pie(x=x1, labels=labels1, explode=[0, 0.2])
        st.pyplot(fig1)

        st.subheader("Distribution for Gender")
        x2 = census_df["gender"].value_counts()
        labels2 = x2.index
        fig2 = plt.figure(figsize=(12, 5))
        plt.pie(x=x2, labels=labels2, explode=[0, 0.2])
        st.pyplot(fig2)

    # Display box plot using matplotlib module and 'st.pyplot()'
    if (plots == "Box Plot"):
        st.subheader("Box Plot for hours-per-week")
        fig1 = plt.figure(figsize=(12, 5))
        sns.boxplot(x="hours-per-week", y="gender", data=census_df)
        st.pyplot(fig1)

        fig2 = plt.figure(figsize=(12, 5))
        sns.boxplot(x="hours-per-week", y="income", data=census_df)
        st.pyplot(fig2)

    # Display count plot using seaborn module and 'st.pyplot()' 
    if (plots == "Count Plot"):
        st.subheader("Count Plot for workclass")
        fig = plt.figure(figsize=(12, 5))
        sns.countplot(census_df["workclass"])
        st.pyplot(fig)
