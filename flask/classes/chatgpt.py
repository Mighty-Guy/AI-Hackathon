import openai
import yaml
from yaml.loader import SafeLoader

initPrompt = [
    {"role": "system", "content": "You are a storyteller. Generate a text-based game adventure with multiple stages. I can make decisions with free text. Wait for my decision at every stage."}
]


class ChatGPT():
    def __init__(self):
        # Reading YAML data
        file_name = 'resources/secrets.yml'
        with open(file_name, 'r') as f:
            secrets = yaml.load(f, Loader=SafeLoader)
        openai.api_key = secrets['chatgpt']
        self.conversation = initPrompt

    def get_story(self, prompt):
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

    def get_music(self):
        conversation_music = self.conversation.copy()
        conversation_music.append(
            {"role": "user", "content": "Give me a genre of music that fits the current situation in the story. Answer in a single word."})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_music,
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        # remove punctuation
        result = result.replace('.', '')
        return result

    def get_conversation(self):
        return self.conversation

    def reset_conversation(self):
        self.conversation = initPrompt


# chat = ChatGPT()
# chat.get_story("Start game")
# chat.get_response("Take option 1")
# print(chat.get_music())
# print(chat.get_conversation())
