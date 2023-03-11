import dash
from dash import dcc
from dash import html
import pyaudio as pyaudio
import pyaudio

import wave
from pydub import AudioSegment



def getMicrophoneComponent():
    return html.Div([
        html.H3("Record MP3"),
        html.Button("Start Recording", id="record-button"),
        html.Button("Stop Recording", id="stop-button"),
        dcc.Interval(id="update-interval", interval=1000),
        dcc.Interval(id="update-interval-2", interval=1000),
    ])

audio = pyaudio.PyAudio()
stream = None
frames = []


# Initialize the audio stream
audio = pyaudio.PyAudio()
stream = None
frames = []

# Define a callback to start recording audio
def start_recording(n_clicks):
    print('start recording', n_clicks)
    global stream, frames
    if n_clicks is None:
        return True
    else:
        # Open the audio stream
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        return False

# Define a callback to stop recording audio and save the file
def stop_recording(n_clicks):
    print('stop recording')
    global stream, frames
    if n_clicks is None or stream is None:
        return True
    else:
        # Close the audio stream
        stream.stop_stream()
        stream.close()

        # Save the audio frames to a WAV file
        wf = wave.open("output.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Convert the WAV file to an MP3 file
        sound = AudioSegment.from_wav("output.wav")
        sound.export("output.mp3", format="mp3")

        # Reset the global variables
        stream = None
        frames = []

        return False

# Define a callback to continuously update the app
def update_app(n):
    if stream is None:
        return 1000
    else:
        # Read audio frames from the stream
        data = stream.read(1024)
        frames.append(data)
        return 0
