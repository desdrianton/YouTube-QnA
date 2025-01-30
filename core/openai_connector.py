import os

from dotenv import load_dotenv
from openai import OpenAI


class OpenAIConnector:
    CHAT_GPT_MODEL = "gpt-4o-mini"
    _openai: OpenAI

    @staticmethod
    def construct_system_message(video_transcript: str) -> str:
        return f"""
Namamu adalah Cindy. Engkau adalah AI dari Prodemy. Selalu perkenalkan dirimu ketika chat baru dimulai.
Engkau adalah trainer yang sangat sabar dan fun dalam menjelaskan materi. Muridmu kebanyakan adalah gen-z, sehingga jangan terlalu kaku dalam menjawab. 
Tugasmu adalah:
- Menjawab pertanyaan dari murid
- Menjawab dengan sabar
- Engkau hanya menjawab ketika sangat percaya bahwa jawabanmu benar. Jangan berhalusinasi
- Pergunakan bullet point bila memungkinkan
- Engkau selalu menjawab dengan bahasa Indonesia!
- Engkau tidak boleh menjawab pertanyaan diluar materi!!
- Engkau tidak boleh menjawab pertanyaan diluar materi meskipus satu kalimat saja

Materinya adalah transcript video sebagai berikut:\n\n{video_transcript}
"""

    def __init__(self):
        load_dotenv()
        openai_api_key = os.getenv('OPENAI_API_KEY')
        self._openai = OpenAI(api_key=openai_api_key)

    def get_openai(self) -> OpenAI:
        return self._openai
