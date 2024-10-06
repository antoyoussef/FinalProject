# app.py

import streamlit as st
import predict_page
import explore_page

# Streamlit App for navigation between pages
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Predict Trouble Sleeping", "Explore Dataset"])

    if selection == "Predict Trouble Sleeping":
        predict_page.main()
    elif selection == "Explore Dataset":
        explore_page.main()

if __name__ == "__main__":
    main()
