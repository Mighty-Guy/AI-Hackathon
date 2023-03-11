import replicate
import os

import yaml
from yaml.loader import SafeLoader

# Reading YAML data
file_name = 'flask/resources/secrets.yml'
with open(file_name, 'r') as f:
    secrets = yaml.load(f, Loader=SafeLoader)

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = secrets['whisper']

model = replicate.models.get("openai/whisper")
version = model.versions.get("e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc")
# https://replicate.com/openai/whisper/versions/e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc#input
inputs = {
    # Audio file
     'audio': open("test-resources/Kennedy_berliner.ogg.mp3", "rb"),

    # Choose a Whisper model.
    'model': "large-v2",

    # Choose the format for the transcription
    'transcription': "plain text",

    # Translate the text to English when set to True
    'translate': False,

    # language spoken in the audio, specify None to perform language
    # detection
    # 'language': ...,

    # temperature to use for sampling
    'temperature': 0,

    # optional patience value to use in beam decoding, as in
    # https://arxiv.org/abs/2204.05424, the default (1.0) is equivalent to
    # conventional beam search
    # 'patience': ...,

    # comma-separated list of token ids to suppress during sampling; '-1'
    # will suppress most special characters except common punctuations
    'suppress_tokens': "-1",

    # optional text to provide as a prompt for the first window.
    # 'initial_prompt': ...,

    # if True, provide the previous output of the model as a prompt for
    # the next window; disabling may make the text inconsistent across
    # windows, but the model becomes less prone to getting stuck in a
    # failure loop
    'condition_on_previous_text': True,

    # temperature to increase when falling back when the decoding fails to
    # meet either of the thresholds below
    'temperature_increment_on_fallback': 0.2,

    # if the gzip compression ratio is higher than this value, treat the
    # decoding as failed
    'compression_ratio_threshold': 2.4,

    # if the average log probability is lower than this value, treat the
    # decoding as failed
    'logprob_threshold': -1,

    # if the probability of the <|nospeech|> token is higher than this
    # value AND the decoding has failed due to `logprob_threshold`,
    # consider the segment as silence
    'no_speech_threshold': 0.6,
}

# https://replicate.com/openai/whisper/versions/e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc#output-schema
output = version.predict(**inputs)
print(output)
print(output.get("transcription"))

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = output.get("transcription")

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False, tld='us')

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("test-resources/to_speech.mp3")

# Playing the converted file
os.system("start test-resources/to_speech.mp3")
