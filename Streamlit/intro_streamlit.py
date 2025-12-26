import streamlit as st # Import the Streamlit library

# Set the title of the app
st.title('My First Streamlit App created by Munaiah Kona')

# Display a welcome message
st.write("Welcome , This app calculate the square of a number in Streamlit!")

# Input: Slider to select a number
st.header('Select a number to square:')

# Slider ranging from 0 to 100 with a default value of 10
number = st.slider('Select a number', 0, 100, 10)

# Display the result
st.subheader('Result')

# Calculate the square of the selected number
squared_value = number * number

# Display the squared value
st.write(f'The square of {number} is {squared_value}')

# Add a footer  
st.write("Thank you for using this app!")