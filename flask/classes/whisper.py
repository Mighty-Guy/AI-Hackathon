import replicate
import os

import yaml
from yaml.loader import SafeLoader


class Whisper:

    def __init__(self):
        # Reading YAML data
        file_name = 'dash/secrets.yml'
        with open(file_name, 'r') as f:
            secrets = yaml.load(f, Loader=SafeLoader)
        os.environ["REPLICATE_API_TOKEN"] = secrets['whisper']
        self.model = replicate.models.get("openai/whisper")
        self.version = self.model.versions.get("e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc")

        self.inputs = {
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

    def get_transcript(self):
        return self.version.predict(**self.inputs).get("transcription")

    def set_input(self, audio_path):
        self.inputs['audio'] = open(audio_path, "rb")
        return self.get_transcript()
