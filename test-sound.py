from sclib import SoundcloudAPI, Track, Playlist
from dash.components.soundCloud_extended import SoundCloudAPI_V2

api_v2 = SoundCloudAPI_V2()
api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library
interpret = 'itsmeneedle'
song = 'sunday-morning'

list = api_v2.search(to_search='scary', genres='Pop')

track = api.resolve('https://soundcloud.com/' + interpret + '/' + song)

assert type(track) is Track

filename = f'./{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as file:
    track.write_mp3_to(file)