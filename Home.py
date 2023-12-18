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
    - [x] RAG system
    - [x] Quizz creator

    **TODO:**
    - [ ] Multible documents
    - [ ] 5-10 shot learning

    ## Mistral
    Mistral interface

    **TODO:**
    - [ ] RAG support
    - [ ] 5-10 shot learning
    """
)
