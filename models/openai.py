from openai import OpenAI

class Generator:
    def __init__(self, api_key, base_url):
        base_url = base_url.rstrip('/')
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
    def set_model(self, model):
        self.model = model
        
    def generate_response(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content
        
    def json_response(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type":"json_object"}
        )
        return response.choices[0].message.content
