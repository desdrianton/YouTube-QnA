import gradio as gr
from openai import OpenAI

from code.llm_connector import construct_system_message, CHAT_GPT_MODEL

chat_gpt: OpenAI


def print_info(*, query_params: str, history, messages):
    print(f"{'.' * 100} {query_params}")
    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)


def chat(message, history, request: gr.Request):
    messages = (
            [{"role": "system", "content": construct_system_message(video_transcript="")}] +
            history +
            [{"role": "user", "content": message}]
    )

    print_info(query_params=request.query_params, history=history, messages=messages)

    stream = chat_gpt.chat.completions.create(model=CHAT_GPT_MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


def setup_gradio_ui(openai: OpenAI):
    global chat_gpt
    chat_gpt = openai

    gr.ChatInterface(fn=chat, type="messages").launch()
