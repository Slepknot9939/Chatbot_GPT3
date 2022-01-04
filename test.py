import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('API_KEY')


completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt,
        engine="davinci",
        stop=['\nHuman'],
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=3,
        max_tokens=1000)
    answer = response.choices[0].text.strip()
    return answer
    