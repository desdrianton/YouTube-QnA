import gradio as gr

from code.openai_connector import OpenAIConnector
from code.yt_transcript import YTTranscript


class GradioUI:
    _openai_connector: OpenAIConnector
    _yt_transcript: YTTranscript

    def __init__(self, openai_connector: OpenAIConnector, yt_transcript: YTTranscript):
        self._openai_connector = openai_connector
        self._yt_transcript = yt_transcript

    def _chat(self, message, history, request: gr.Request):
        query_params: dict = dict(request.query_params)
        print(f"query_params: {query_params.get("video_id")}")
        video_id = query_params.get("video_id")
        video_transcript = self._yt_transcript.get_transcript(video_id)

        messages = (
                [{"role": "system", "content": self._openai_connector.construct_system_message(video_transcript=video_transcript)}] +
                history +
                [{"role": "user", "content": message}]
        )

        stream = self._openai_connector.get_openai().chat.completions.create(
            model=self._openai_connector.CHAT_GPT_MODEL, messages=messages, stream=True)

        response = ""
        for chunk in stream:
            response += chunk.choices[0].delta.content or ''
            yield response

    def launch(self):
        gr.ChatInterface(fn=self._chat, type="messages").launch()
