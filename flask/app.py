
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

game_options = {0: 'random', 1: 'adventure', 2: 'sci-fy'}


@app.route('/')
def index():
    return render_template('index.html', game_options=game_options)

@app.route('/play')
def play():
    if 'game_option' in request.args:
        option = request.args['game_option']
    else:
        option = 0 # default is random

    #add chatgpt
    #play sound
    #styling
    return render_template('play.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    file = request.files['audio']
    file.save('audio.webm')
    #
    return 'OK'

@app.route('/audio/<path:path>')
def serve_audio(path):
    return send_from_directory('../test-resources/', 'Kennedy_berliner.ogg.mp3')

if __name__ == '__main__':
    app.run()