import streamlit as st

st.set_page_config(
    page_title="Quizz creator",
)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    # Research

    Select a model from the sidebar to get started. 

    ## GPT
    - RAG Quizz creator

    ## Mistral
    - Vanilla Mistral interface

    """
)
