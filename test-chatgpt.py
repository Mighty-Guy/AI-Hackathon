import os
import openai
import yaml
from yaml.loader import SafeLoader

# Reading YAML data
file_name = 'aihackaton/secrets.yml'
with open(file_name, 'r') as f:
    secrets = yaml.load(f, Loader=SafeLoader)



openai.api_key = secrets['chatgpt']


def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response['choices'][0]['text']