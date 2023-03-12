from sclib import SoundcloudAPI, Track, Playlist
import sys
import json
from ssl import SSLContext
from urllib.request import urlopen

SSL_VERIFY=True

def eprint(*values, **kwargs):
    """ Print to stderr """
    print(*values, file=sys.stderr, **kwargs)

def get_obj_from(url):
    """ Get object from url """
    try:
        return json.loads(get_page(url))
    except Exception as exc:  # pylint: disable=broad-except
        eprint(type(exc), str(exc))
        return False

def get_page(url):
    """ get text from url """
    return get_url(url).decode('utf-8')

def get_url(url):
    """ Get url """
    with urlopen(url, context=get_ssl_setting()) as client:
        text = client.read()
    return text

def get_ssl_setting():
    """ Get ssl context """
    if SSL_VERIFY:
        return None
    return SSLContext()


class SoundCloudAPI_V2(SoundcloudAPI):

    SEARCH_URL_V2 = "https://api-v2.soundcloud.com/search?q={query}&genres={genres}&tags={tags}&client_id={client_id}&limit={limit}"

    def search(self, to_search, genres, tags='scary', limit=10):
        """ Resolve url """
        if not self.client_id:
            self.get_credentials()
        url = self.SEARCH_URL_V2.format(
            query=to_search,
            limit=limit,
            genres=genres,
            tags=tags,
            client_id=self.client_id
        )
        track_list = []
        obj = get_obj_from(url)
        for song in obj['collection']:
            if 'track_format' in song:
                if song['track_format'] == 'single-track':
                    track_list.append(song['id'])
        return track_list