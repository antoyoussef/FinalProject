# explore_page.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (you should replace this with the actual path to your dataset)
sleep_df = pd.read_csv('NPHA-doctor-visits.csv')

# Streamlit App for data exploration
def main():
    st.title("Dataset Exploration")

    # Show the dataset
    if st.checkbox("Show raw data"):
        st.write(sleep_df)

    # Feature selection for visualization
    st.write("## Visualize the data")
    selected_x = st.selectbox('Select X-axis variable', sleep_df.columns)
    selected_y = st.selectbox('Select Y-axis variable', sleep_df.columns)

    plot_type = st.selectbox('Select plot type', ['Scatter Plot', 'Bar Plot', 'Box Plot'])

    # Scatter Plot
    if plot_type == 'Scatter Plot':
        st.write(f"Scatter plot of {selected_x} vs {selected_y}")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=sleep_df, x=selected_x, y=selected_y)
        st.pyplot(plt)

    # Bar Plot
    if plot_type == 'Bar Plot':
        st.write(f"Bar plot of {selected_x} vs {selected_y}")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=sleep_df, x=selected_x, y=selected_y)
        st.pyplot(plt)

    # Box Plot
    if plot_type == 'Box Plot':
        st.write(f"Box plot of {selected_x} vs {selected_y}")
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=sleep_df, x=selected_x, y=selected_y)
        st.pyplot(plt)

if __name__ == "__main__":
    main()
