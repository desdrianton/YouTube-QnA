from core.gradio_ui import GradioUI
from core.openai_connector import OpenAIConnector
from core.yt_transcript import YTTranscript


class Cindy:
    _openai_connector: OpenAIConnector
    _yt_transcript: YTTranscript
    _gradio_ui: GradioUI

    @staticmethod
    def _print_cindy_header():
        print(f"{'=' * 120}")
        print("Booting CINDY Server")
        print("CINDY (Curiosity, Inspiration, Navigation, and Development for You)")
        print("CINDY is an AI Server for Prodemy's LXP")
        print(f"{'=' * 120}")

    def __init__(self):
        self._openai_connector = OpenAIConnector()
        self._yt_transcript = YTTranscript()
        self._gradio_ui = GradioUI(openai_connector=self._openai_connector, yt_transcript=self._yt_transcript)

    def launch(self):
        Cindy._print_cindy_header()
        self._gradio_ui.launch()
