from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library
interpret = 'itsmeneedle'
song = 'sunday-morning'

track = api.resolve('https://soundcloud.com/' + interpret + '/' + song)

assert type(track) is Track

filename = f'./{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as file:
    track.write_mp3_to(file)