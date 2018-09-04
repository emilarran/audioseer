from django.shortcuts import render
from django.views import View
from preprocessing.models import MusicTrack
from django.http import HttpResponse
import csv
import datetime
import requests
import json


class ReadFromDataSetView(View):
    def get(self, request, *args, **kwargs):
        with open('dataset.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = [(int(col1), int(col4), col5.split('/')[4], datetime.datetime.strptime(col6, "%Y-%m-%d").date()) for col1, col2, col3, col4, col5, col6, col7 in reader]
            for item in data:
                track = MusicTrack.objects.create(
                    rank=item[0],
                    streams=item[1],
                    track_id=item[2],
                    date=item[3])

                track.save()
        return HttpResponse('ok')


class SpotifyAPIView(View):
    def get(self, request, *args, **kwargs):
        tracks = MusicTrack.objects.filter(duration_ms=None)[:100]
        token = input('INPUT SPOTIFY OAUTH TOKEN: ')
        while tracks:
            ids = ''
            for track in tracks:
                ids = ids + track.track_id + ','
            ids = ids[:-1]
            payload = {
                'ids': ids
            }
            headers = {
                'Authorization': 'Bearer ' + token
            }
            ret = requests.get(
                'https://api.spotify.com/v1/audio-features',
                params=payload,
                headers=headers
            )
            if ret.status_code == 200:
                trackinfos = json.loads(ret.text)
                audiofeatures = trackinfos['audio_features']
                i = 0
                for track in tracks:
                    track.danceability = audiofeatures[i]['danceability']
                    track.energy = audiofeatures[i]['energy']
                    track.key = audiofeatures[i]['key']
                    track.loudness = audiofeatures[i]['loudness']
                    track.mode = audiofeatures[i]['mode']
                    track.speechiness = audiofeatures[i]['speechiness']
                    track.acousticness = audiofeatures[i]['acousticness']
                    track.instrumentalness = audiofeatures[i]['instrumentalness']
                    track.liveness = audiofeatures[i]['liveness']
                    track.valence = audiofeatures[i]['valence']
                    track.tempo = audiofeatures[i]['tempo']
                    track.duration_ms = audiofeatures[i]['duration_ms']
                    track.time_signature = audiofeatures[i]['time_signature']

                    print(dir(track))

                    track.save()
                    i = i + 1

                tracks = MusicTrack.objects.filter(duration_ms=None)[:100]

            else:
                print('GET NEW OAUTH TOKEN FROM SPOTIFY')
                token = input('INPUT SPOTIFY OAUTH TOKEN: ')

        return HttpResponse('ok')
