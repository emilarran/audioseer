from django.shortcuts import render
from preprocessing.models import MusicTrack
from sklearn.preprocessing import MinMaxScaler
from django.views import View
from django.http import HttpResponse


class TrainingView(View):
    def get(self, request, *args, **kwargs):
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform([
            track.numpyArray for track in MusicTrack.objects.all()
        ])
        print(scaled)
        return HttpResponse('ok')
