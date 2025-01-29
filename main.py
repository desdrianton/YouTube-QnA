import gradio as gr
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI(api_key=openai_api_key)
system_message = """
Engkau adalah orang yang sangat lucu dan sabar.
Engkau hanya menjawab ketika sangat percaya bahwa jawabanmu benar. Jangan berhalusinasi 
Engkau selalu menjawab dengan bahasa Indonesia! 
"""

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

    stream = openai.chat.completions.create(model="gpt-4o-mini", messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


def main():
    gr.ChatInterface(fn=chat, type="messages").launch()


if __name__ == '__main__':
    main()
