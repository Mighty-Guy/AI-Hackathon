from gtts import gTTS


class T2S:
    def __init__(self):
        self.language = "en"
        self.tld = "us"
        self.slow = False
        self.text = ""

    def set_language(self, new_language):
        self.language = new_language

    def set_tld(self, new_tld):
        self.tld = new_tld

    def get_speech(self, text, path):
        obj = gTTS(text=text, lang=self.language, slow=self.slow, tld=self.tld)
        obj.save(path)
