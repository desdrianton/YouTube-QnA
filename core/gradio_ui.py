import gradio as gr

from core.openai_connector import OpenAIConnector
from core.yt_transcript import YTTranscript


class GradioUI:
    _openai_connector: OpenAIConnector
    _yt_transcript: YTTranscript

    def __init__(self, openai_connector: OpenAIConnector, yt_transcript: YTTranscript):
        self._openai_connector = openai_connector
        self._yt_transcript = yt_transcript

    def _chat(self, message, history, request: gr.Request):
        query_params: dict = dict(request.query_params)
        print(f"video_id: {query_params.get("video_id")}")
        video_id = query_params.get("video_id")
        video_transcript = self._yt_transcript.get_transcript(video_id)

        messages = (
                [{"role": "system",
                  "content": self._openai_connector.construct_system_message(video_transcript=video_transcript)}] +
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
        force_light_mode = """
        function refresh() {
            const url = new URL(window.location);
            if (url.searchParams.get('__theme') !== 'light') {
                url.searchParams.set('__theme', 'light');
                window.location.href = url.href;
            }
        }
        """

        hide_footer = """footer{display:none !important}"""
        gr.ChatInterface(fn=self._chat, type="messages",
                         title="Cindy AI",
                         description="<center>Curiosity, Inspiration, Navigation, and Development for You</center",
                         js=force_light_mode,
                         css=hide_footer).launch()
