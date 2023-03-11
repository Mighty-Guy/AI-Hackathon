import time
import openai
import yaml
from yaml.loader import SafeLoader

# Reading YAML data
file_name = 'dash/secrets.yml'
with open(file_name, 'r') as f:
    secrets = yaml.load(f, Loader=SafeLoader)
openai.api_key = secrets['chatgpt']


class ChatGPT():
    def __init__(self):
        self.conversation = [
            {"role": "system", "content": "You are a storyteller. Generate a text-based game adventure with 10 stages and 4 options per stage. Wait for my response at every stage."}
        ]

    def get_response(self, prompt):
        self.conversation.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.conversation,    
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        self.conversation.append({"role": "system", "content": result})
        return result

    def get_conversation(self):
        return self.conversation
    
    def reset_conversation(self):
        self.conversation = [
            {"role": "system", "content": "You are a storyteller. Generate a text-based game adventure with 10 stages and 4 options per stage. Wait for my response at every stage."}
        ]
    
chat = ChatGPT()
chat.get_response("Start game")
chat.get_response("Take option 1")

print(chat.get_conversation())
