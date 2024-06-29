import streamlit as st

# Set the configuration for the Streamlit app
st.set_page_config(page_title="Data Manager", page_icon=":material/edit:")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "ChatBot"])

# Page selection
if page == "Home":
    st.title("Home")
    st.write("Welcome to the Data Manager App!")
elif page == "ChatBot":
    from App1 import chatbot
    chatbot.run()
