import streamlit as st

st.set_page_config(page_title="Mental Health Chatbot", page_icon="💬")
st.title("💬 Mental Health Chatbot")
st.write("I'm here to talk. How are you feeling today?")

user_input = st.text_input("You:")

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "stress" in user_input:
        return "It's okay to feel stressed. Try deep breathing or a short walk. 🌿"
    elif "sleep" in user_input:
        return "Avoid screens before bed and try calming music. 😴"
    elif "anxiety" in user_input:
        return "Take a few deep breaths. You're not alone in this. 🌬️"
    elif "mental health" in user_input:
        return "Mental health matters. Talking is a great first step. ❤️"
    elif "sad" in user_input or "depressed" in user_input:
        return "I'm here for you. Please talk to someone you trust. 💛"
    elif "happy" in user_input:
        return "That's great! Stay positive and spread the joy. 🌟"
    elif "bye" in user_input:
        return "Take care! You're doing your best, and that’s what counts. 💪"
    else:
        return "I'm still learning. Maybe try saying it differently? 🤗"

if user_input:
    response = get_bot_response(user_input)
    st.write(f"**Bot:** {response}")
 
 !pip install streamlit
