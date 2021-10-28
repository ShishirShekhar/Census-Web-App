# Import necessary modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df, plot_list):
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


def view_data(df):
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
