from flask import Flask, request, send_from_directory, render_template, jsonify
from classes.chatgpt import ChatGPT
from classes.whisper import Whisper
from classes.soundcloud import SoundCloudAPI_V2
import os
from classes.t2s import T2S

soundcloud = SoundCloudAPI_V2()
chat = ""
game_text = ''

app = Flask(__name__)

game_options = {0: 'random', 1: 'adventure', 2: 'sci-fy'}

game_text_gpt_list = []
game_user_answers_list = []

whipser = Whisper()
t2s = T2S()


@app.route('/')
def index():
    return render_template('index.html', game_options=game_options)

@app.route('/play')
def play():
    global chat, t2s
    game_text_gpt_list.clear()
    game_user_answers_list.clear()

    if 'game_option' in request.args:
        option = int(request.args['game_option'])
    else:
        option = 0 # default is random
    

    chat = ChatGPT(game_option=option)
    game_text = chat.get_story("Start game")
    game_text_gpt_list.append(game_text)
    music_genre = chat.get_music()
    soundcloud_list = soundcloud.search(to_search=music_genre, genres=music_genre)

    t2s.get_speech(game_text, './resources/audio-answer.mp3')


    return render_template('play.html', game_text_gpt_list=game_text_gpt_list, game_user_answers_list=game_user_answers_list, sound_cloud_id=soundcloud_list[0], play_music=True)

@app.route('/save-audio', methods=['POST'])
def save_audio():
    global game_user_answers_list, game_text_gpt_list, whisper, chat, t2s
    file = request.files['audio']
    file.save('audio.webm')
    text = whipser.set_input('audio.webm')
    game_user_answers_list.append(text)
    game_text = chat.get_story(text)
    game_text_gpt_list.append(game_text)
    t2s.get_speech(game_text, './resources/audio-answer.mp3')
    return 'OK'

@app.route('/audio/<path:text>')
def serve_audio(text):
    return send_from_directory('./resources/', "audio-answer.mp3")

@app.route('/chat/gpt/newest')
def get_newest_gpt_answer():
    return jsonify({"text": game_text_gpt_list[-1]})

@app.route('/chat/user/newest')
def get_newest_user_answer():
    return jsonify({"text": game_user_answers_list[-1]})

if __name__ == '__main__':
    app.run()