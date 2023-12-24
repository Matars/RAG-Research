# RAG Quizz Creator

## Quickstart

```bash
git clone https://github.com/Matars/RAG-Research
pip install -r requirments
streamlit run GPT.py
```

## Description

This project provides an interface3 for a quizz creator Assisntant

## File descriptions

This project is a Python-based application designed to create quizzes. It uses models from OpenAI to generate questions. The project structure is as follows:

- [`GPT.py`](GPT.py): The landing page of the application, and the main chatbot interface for creating the quizzes.
- [`createAssistant.ipynb`](createAssistant.ipynb): A Jupyter notebook used to create an OpenAI assistant and manage files. The generated assistant ID is used within the application.
- [`responses.py`](responses.py): Contains all the API calls to different models.
- [`assistant_ids.txt`](assistant_ids.txt): Holds the assistant IDs that are needed to use the assistant API.
- [`.env.example`](.env.example): An example environment file. Fill in your own values and rename this to `.env` to use it.
