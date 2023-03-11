from flask import Flask, render_template, request
import pyaudio
import wave

@app.route('/record')
def record():
    return render_template('play.html')