from django.shortcuts import render

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

#入力パート
track_url = 'https://open.spotify.com/track/7nLAfMQtlDHII3wczJH9C2'

def sample(request):
    if request.method == "POST":
        if "start_button" in request.POST:
            #以下Stratした後の処理
            track_url = 'input1'
        elif "finish_button" in request.POST:
            #以下finishした後の処理
            track_url = 'https://open.spotify.com/track/7nLAfMQtlDHII3wczJH9C2'

#認証パート
my_id ='ce054fd7124d476a854843ffc6f18f5f' #client ID
my_secret = '0bdc964c680f4008b00dfb242497f7c6' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

#出力パート
track_data = spotify.track(track_url)
time.sleep(1)
results = spotify.audio_features(track_url)
result = results[0]
pitch_class = {0:'C', 1:'C#', 2:'D', 3:'D#', 4:'E', 5:'F',
               6:'F#', 7:'G', 8:'G#', 9:'A', 10:'A#', 11:'B'}
mode_dec = {0:'Minor', 1:'Major'}
ptich = pitch_class[result['key']]
mode_m = mode_dec[result['mode']] #Minor ot Major
track_ms = result['duration_ms'] #track duration msec
track_s = track_ms/1000 #曲長さ sec track duration sec
track_min = track_s//60 #曲長さ min track duration min
track_min_sec = track_s -60 * track_min #曲長さ min track duration min

def index(request):
    params = {
        'name':"Kintarou",
        'page':'track',
    }
    return render(request,'webtestapp/index.html',params)
def track(request):
    params = {
        'artist_name':track_data['album']['artists'][0]['name'],
        'track_data':track_data['name'],
        'popularity':str(track_data['popularity']),
        'track_time_m':track_min,
        'track_time_s':track_min_sec,
        'page':'track',
    }
    return render(request,'webtestapp/index.html',params)
