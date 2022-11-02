import requests
from decouple import config


TOKEN_API = config('TOKEN_API')


def search_spotify(song):
    url = "https://spotify23.p.rapidapi.com/search/"
    querystring = {f"q": {song}, "type": "tracks", "offset": "0", "limit": "1", "numberOfTopResults": "1"}
    headers = {
        "X-RapidAPI-Key": TOKEN_API,
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    name_track = response['tracks']['items'][0]['data']['name']
    spotify_track = response['tracks']['items'][0]['data']['uri']
    id_track = response['tracks']['items'][0]['data']['id']
    artist = response['tracks']['items'][0]['data']['artists']['items'][0]['profile']['name']
    image_track = response['tracks']['items'][0]['data']['albumOfTrack']['coverArt']['sources'][0]['url']
    return id_track, name_track, artist, spotify_track, image_track





