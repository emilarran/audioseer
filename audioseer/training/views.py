from django.shortcuts import render
from preprocessing.models import MusicTrack
from sklearn.preprocessing import MinMaxScaler
from django.views import View
from django.http import HttpResponse
from keras.models import Sequential
from keras.layers import Dense, Dropout
import random
import matplotlib.pyplot as plt
import numpy as np


class TrainingView(View):
    def get(self, request, *args, **kwargs):
        scaler = MinMaxScaler()
        trackdata = [track.numpyArray for track in MusicTrack.objects.all()]
        random.shuffle(trackdata)
        toscale = []
        labels = []
        for track in trackdata:
            toscale.insert(
                len(toscale),
                [track[0], track[1], track[2], track[3], track[4]])
            labels.insert(len(labels), [track[5], track[6]])

        scaled = scaler.fit_transform(toscale)
        labels = np.asarray(labels)
        print(labels.shape)
        model = Sequential()
        model.add(Dense(units=1200, input_dim=5, activation='softmax'))
        model.add(Dropout(0.4))
        model.add(Dense(2, activation='softmax'))
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        history = model.fit(
            scaled, labels, validation_split=0.33, epochs=500, batch_size=200)
        print(history.history.keys())
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.legend(['train', 'test'])
        plt.show()
        score = model.evaluate(scaled[51940:], labels[51940:], batch_size=10)
        print(score)
        import pdb; pdb.set_trace()

        return HttpResponse('ok')
