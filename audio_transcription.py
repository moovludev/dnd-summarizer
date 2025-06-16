from openai import OpenAI

class OpenAiClient:
    def __init__(self, api_key:str):
        self.client = OpenAI(api_key=api_key)

    def validate_api_key(self):
        raise NotImplementedError
    
    def transcribe_text(self):
        raise NotImplementedError
    
