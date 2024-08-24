import streamlit as st
import time

# Set the title
st.title("Customer Support System")


# ask for user prompt and display the message
if user_prompt := st.chat_input("Say Something"):
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # sleep for 1.5 seconds before responding
    time.sleep(1.5)
    with st.chat_message("assistant"):
        st.markdown(user_prompt)

