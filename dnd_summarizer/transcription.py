import logging
import pathlib
from openai import OpenAI

logger = logging.getLogger("dnd_summarizer-transcription")


class OpenAiClient:
    def __init__(self, api_key:str, model="whisper-1", language="en"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.language = language

    def transcribe_text(self, filename:pathlib.Path) -> dict:
        logger.info("Processing %s", filename)
        output = self.client.audio.transcriptions.create(
            file=filename, model=self.model, language=self.language, response_format="verbose_json"
        )
        return self._format_transcription(output)

    def _format_transcription(self, transcription:dict) -> dict:
        # TODO: Reformat transcription
        return {0:transcription}
