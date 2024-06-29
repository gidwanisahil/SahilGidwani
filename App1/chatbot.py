import streamlit as st

def run():
    st.title("ChatBot")
    st.write("Welcome to the ChatBot!")
    
    # User input text box
    user_input = st.text_input("You: ", "")
    
    if user_input:
        st.write("Bot: ", generate_response(user_input))

# Dummy function to simulate chatbot response generation
def generate_response(user_input):
    # For now, it just echoes the input
    return f"Echo: {user_input}"
