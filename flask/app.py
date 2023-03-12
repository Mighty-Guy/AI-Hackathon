from flask import Flask, request, send_from_directory, render_template, jsonify
from classes.chatgpt import ChatGPT
from classes.whisper import Whisper

from classes.t2s import T2S

chat = ""
game_text = ''
app = Flask(__name__)

game_options = {0: 'random', 1: 'adventure', 2: 'sci-fy'}

game_text_gpt_list = []
game_user_answers_list = []


@app.route('/')
def index():
    return render_template('index.html', game_options=game_options)

@app.route('/play')
def play():
    if 'game_option' in request.args:
        option = request.args['game_option']
    else:
        option = 0 # default is random
    
    print('Option: ' + str(option))
    
    chat = ChatGPT(option)
    game_text = chat.get_story("Start game")
    game_text_gpt_list.append(game_text)
    return render_template('play.html', game_text_gpt_list=game_text_gpt_list, game_user_answers_list=game_user_answers_list)

@app.route('/save-audio', methods=['POST'])
def save_audio():
    global game_user_answers_list, game_text_gpt_list
    file = request.files['audio']
    file.save('audio.webm')
    whipser = Whisper()
    text = whipser.set_input('audio.webm')
    game_user_answers_list.append(text)
    print(text)
    game_text = chat.get_story(text)
    game_text_gpt_list.append(game_text)
    print(game_text)
    t2s = T2S()
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