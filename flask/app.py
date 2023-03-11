
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/record')
def record():
    return render_template('record.html')


@app.route('/save-audio', methods=['POST'])
def save_audio():
    file = request.files['audio']
    file.save('audio-sabrina.webm')
    return 'OK'

@app.route('/audio/<path:path>')
def serve_audio(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run()