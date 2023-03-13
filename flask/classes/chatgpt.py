import openai
from get_docker_secret import get_docker_secret

initContent = "You are a storyteller. Generate a text-based {} game with multiple stages. I can make decisions with free text. Wait for my decision at every stage."

game_options = {0: '', 1: 'adventure', 2: 'sci-fy'}


class ChatGPT():
    def __init__(self, game_option=0):
        openai.api_key = get_docker_secret('CHATGPT_SECRET', default='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')
        self.conversation = [{"role": "system", "content": initContent.format(game_options[game_option])}]
        print(self.conversation)

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

    def reset_conversation(self, game_option=0):
        self.conversation = [{"role": "system", "content": initContent.format(game_options[game_option])}]


chat = ChatGPT(1)
# chat.get_story("Start game")
# chat.get_response("Take option 1")
# print(chat.get_music())
# print(chat.get_conversation())
