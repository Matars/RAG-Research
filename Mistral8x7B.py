
"""
This is expirementa and not used in the final product

"""

import streamlit as st
from responses import Mistral7x8BResponse

st.title("Mistral 7x8B Interface")

st.sidebar.info(
    """
    Note: Must set API key in for anyscale .env before using
    API keys are free at anyscale.com
    """
)

# Initialize chat history
if "messages_mistral" not in st.session_state:
    st.session_state.messages_mistral = []

# Display chat messages from history on app rerun
for message in st.session_state.messages_mistral:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages_mistral.append({"role": "user", "content": prompt})

    # Get assistant response
    with st.spinner("Thinking..."):
        response = Mistral7x8BResponse(prompt, messages=st.session_state.messages_mistral)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages_mistral.append({"role": "assistant", "content": response})
