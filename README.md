# RAG Quizz Creator

## Quickstart

```bash
git clone https://github.com/Matars/RAG-Research
pip install -r requirments
streamlit run Home.py
```

## Description

This project provides a flexible and customizable framework for creating and managing interactive quizzes.

## File descriptions

This project is a Python-based application designed to create interactive quizzes. It uses various models from OpenAI to generate questions and evaluate responses. The project structure is as follows:

- [`Home.py`](Home.py): The landing page of the application.
- [`createAssistant.ipynb`](createAssistant.ipynb): A Jupyter notebook used to create an OpenAI assistant. The generated assistant ID is used within the application.
- [`responses.py`](responses.py): Contains all the API calls to different models.
- [`ids.txt`](ids.txt): Holds the assistant and file IDs that are needed to use the assistant API.
- [`pages`](pages/): A directory containing different chatbot interfaces. Each interface is defined in a separate Python script, such as [`GPT.py`](pages/GPT.py) and [`Mistral8x7B.py`](pages/Mistral8x7B.py). These scripts handle the logic for each individual page, including question generation and user interaction.
- [`.env.example`](.env.example): An example environment file. Fill in your own values and rename this to `.env` to use it.
- [`.gitignore`](.gitignore): Specifies intentionally untracked files that Git should ignore.
- [`requirements.txt`](requirements.txt): Lists the Python dependencies that need to be installed with pip.
