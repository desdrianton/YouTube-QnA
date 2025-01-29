from youtube_transcript_api import YouTubeTranscriptApi


class YTTranscript:
    _yt_transcript_dict = {}

    @staticmethod
    def _retrieve_transcript(video_id: str) -> str | None:
        print(f"Retrieving transcript for video id: {video_id}")

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['id'])
            plain_transcript =  " ".join([item['text'] for item in transcript])
            print(f"Length of transcript {video_id} : {len(plain_transcript)}")
            return plain_transcript
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None

    def get_transcript(self, video_id: str) -> str | None:
        if video_id not in self._yt_transcript_dict:
            self._yt_transcript_dict[video_id] = self._retrieve_transcript(video_id)

        return self._yt_transcript_dict[video_id]
