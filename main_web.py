import streamlit as st
import time

# Set the title
st.title("Customer Support System")

# only create messages list if it doesn't exist to save the history of interaction with bot
if "messages" not in st.session_state:
    st.session_state.messages = []

# display history of messages on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

# ask for user prompt and display the message, and append it to the messages list
if user_prompt := st.chat_input("Say Something"):
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append({"role": "user", "message": user_prompt})

    # sleep for 1.5 seconds before responding
    time.sleep(1.5)
    with st.chat_message("assistant"):
        st.markdown(user_prompt)

    st.session_state.messages.append({"role": "assistant", "message": user_prompt})

