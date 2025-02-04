import os

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi


class YTTranscript:
    _yt_transcript_dict = {}
    transcript_source = "local_file" # local_file / youtube

    def __init__(self):
        load_dotenv()
        self.transcript_source = os.getenv('TRANSCRIPT_SOURCE')

    @staticmethod
    def _retrieve_transcript_from_youtube(video_id: str) -> str | None:
        print(f"Retrieving transcript for video id: {video_id}")

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["id", "en"])
            plain_transcript = " ".join([item['text'] for item in transcript])
            print(f"Length of transcript {video_id} : {len(plain_transcript)}")
            print(plain_transcript)
            return plain_transcript
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None

    @staticmethod
    def _retrieve_transcript_from_local_files(video_id: str) -> str:
        try:
            filename = f"transcript_files/{video_id}"
            print(f"Try to read file {filename}")
            f = open(filename, "r")
            transcript = f.read()
            print(f"Length of transcript file {video_id} : {len(transcript)}")
            return transcript
        except Exception as e:
            print(f"Error reading file: transcript_files/{video_id}")
            return None

    def get_transcript(self, video_id: str) -> str | None:
        if video_id not in self._yt_transcript_dict:
            if self.transcript_source == "youtube":
                self._yt_transcript_dict[video_id] = self._retrieve_transcript_from_youtube(video_id)
            elif self.transcript_source == "local_file":
                self._yt_transcript_dict[video_id] = self._retrieve_transcript_from_local_files(video_id)

        return self._yt_transcript_dict[video_id]
