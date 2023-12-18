
from openai import OpenAI
from time import sleep
from dotenv import load_dotenv
import requests
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

load_dotenv()
client = OpenAI()


def Phi2Response(prompt):
    import torch

    torch.set_default_device("cuda")

    model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

    inputs = tokenizer('''def print_prime(n):
    """
    Print all primes between 1 and n
    """''', return_tensors="pt", return_attention_mask=False)

    outputs = model.generate(**inputs, max_length=200)
    text = tokenizer.batch_decode(outputs)[0]
    print(text)


def Mistral7x8BResponse(prompt):
    s = requests.Session()

    api_base = os.getenv("ANYSCALE_BASE_URL")
    token = os.getenv("ANYSCALE_API_KEY")
    url = f"{api_base}/chat/completions"
    body = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": f"{prompt}."}],
        "temperature": 0.7
    }

    with s.post(url, headers={"Authorization": f"Bearer {token}"}, json=body) as resp:
        response = resp.json()
        content = response['choices'][0]['message']['content']
        return content


def OpenAiAssistantResponse(prompt):

    assistantID = "asst_hBggvgQ75jVwE37nchjTVecf"

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistantID,
        instructions="You are a quizz creator that creates quizzes form the provided text ONLY. If the answer cannot be found in the articles, write 'I could not find an answer.'"
    )

    while run.status != "completed":
        print(run.status)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        sleep(2)
    print(run.status)

    # retrieve and format mesasge
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    message = messages.data[0]

    # Extract the message content
    message_content = message.content[0].text
    annotations = message_content.annotations
    citations = []

    # Iterate over the annotations and add footnotes
    for index, annotation in enumerate(annotations):
        # Replace the text with a footnote
        message_content.value = message_content.value.replace(
            annotation.text, f' [{index}]')

        # Gather citations based on annotation attributes
        if (file_citation := getattr(annotation, 'file_citation', None)):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(
                f'[{index}] {file_citation.quote} from {cited_file.filename}')
        elif (file_path := getattr(annotation, 'file_path', None)):
            cited_file = client.files.retrieve(file_path.file_id)
            citations.append(
                f'[{index}] Click <here> to download {cited_file.filename}')
            # Note: File download functionality not implemented above for brevity

    # Add footnotes to the end of the message before displaying to user
    message_content.value += '\n' + '\n'.join(citations)
    return message_content.value


def GeminiResponse(prompt):
    import vertexai
    from vertexai.preview.generative_models import GenerativeModel, Part

    model = GenerativeModel("gemini-pro-vision")
    responses = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        },
        stream=True,
    )

    for response in responses:
        print(response.candidates[0].content.parts[0].text)


if __name__ == "__main__":
    GeminiResponse("Ping!")
