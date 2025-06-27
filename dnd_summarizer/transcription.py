import logging
import os
from openai import OpenAI

logger = logging.getLogger("dnd_summarizer-transcription")


class OpenAiClient:
    def __init__(self, api_key: str, model="whisper-1", language="en"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.language = language

    def transcribe_text(self, filename):
        return self.client.audio.transcriptions.create(
            file=filename, model=self.model, language=self.language, response_format="verbose_json"
        )
