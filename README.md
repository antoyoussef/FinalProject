# Trouble Sleeping Prediction App

This is a web-based application that predicts whether a patient is likely to have trouble sleeping based on their physical health and other sleep-related factors. It allows users to input patient data and receive predictions using a machine learning model. Additionally, the app provides a data exploration feature to visualize relationships within the dataset.

## Project Overview

- **Project Type**: Predictive model
- **Objective**: Accurately predict whether a patient will have trouble sleeping, based on factors such as physical health, pain, stress, and medication.
- **Dataset**: National Poll on Healthy Aging (NPHA) subset focusing on health and sleep.
- **Source**: UC Irvine Machine Learning Repository.
  
The app is built using **Streamlit** and provides two main functionalities:
1. **Prediction Page**: A user-friendly form to input data and get predictions for trouble sleeping.
2. **Exploration Page**: Visualize relationships between features in the dataset.

## Features

- **User Input**: Enter values for physical health, pain, stress, and medication to predict the likelihood of trouble sleeping.
- **Prediction Model**: Based on a pre-trained machine learning model (Gradient Boosting).
- **Data Exploration**: Visualize and explore the dataset with scatter plots, bar plots, and box plots.

## Technologies Used

- **Python**
- **Streamlit** for the web interface.
- **Pandas** for data manipulation.
- **Scikit-learn** for building and deploying the machine learning model.
- **Matplotlib** and **Seaborn** for data visualization.