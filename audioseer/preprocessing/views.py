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
        tracks = MusicTrack.objects.filter(duration_ms=None).all()

        if tracks:
            

        while tracks:
            

        payload = {
            'ids': '0kN8xEmgMW9mh7UmDYHlJP,5uCax9HTNlzGybIStD3vDh,7BKLCZ1jbUBVqRi2FVlTVw,2rizacJSyD9S1IQUxUxnsK,5MFzQMkrl1FOOng9tq6R9r'
        }
        headers = {
            'Authorization': 'Bearer BQDKG-6fZOFd_3MTFKf1KpS82M2F2OgC5flQL1z-yDAEtErktdK2UvjDMmwvCNEQjVZnTR44CaNu3lfiE3btuGJCT9eQJMX1VOR33q8BsgDtSGso_fiZpGK5le1iGO7NRj9LQDmDNq3faEQbUZeaDyiaaijDqVkCEU7ryhVtOaI5Jg'
        }
        ret = requests.get('https://api.spotify.com/v1/audio-features', params=payload, headers=headers)
        data = json.loads(ret.text)
        print(ret)
        import pdb; pdb.set_trace()
        return HttpResponse('ok')
