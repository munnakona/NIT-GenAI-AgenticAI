import streamlit as st # Import the Streamlit library

# Additional libraries for data handling
import pandas as pd  # Import pandas for data manipulation
import numpy as np # Import numpy for numerical operations

# --- App Title and Description ---
st.title("My First Streamlit App")

# App description
st.write("This is a simple app to demonstrate the basic functionalities of Streamlit.")

# --- Interactive Widgets in the Sidebar ---
st.sidebar.header("User Input Features")

# Text Input
user_name = st.sidebar.text_input("What is your name?", "Munaiah Kona")

# Slider
age = st.sidebar.slider("Select your age", 0, 100, 25)

# Selectbox
favorite_color = st.sidebar.selectbox("What is your favorite color?", ["Blue", "Red", "Green", "Yellow"])

# --- Main Page Content ---
st.header(f"Welcome, {user_name}!")
# Display user inputs
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

# --- Displaying Data ---
st.subheader("Here's some random data:")

# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

# --- Checkbox to show/hide content ---
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# --- Button to trigger an action ---
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")
# --- Footer ---
st.write("Thank you for visiting this app!")    