from django.shortcuts import render
from preprocessing.models import MusicTrack
from sklearn.preprocessing import MinMaxScaler
from django.views import View
from django.http import HttpResponse
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

class TrainingView(View):
    def get(self, request, *args, **kwargs):
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(
            [track.numpyArray for track in MusicTrack.objects.all()])
        labels = [track.popularArray for track in MusicTrack.objects.all()]
        labels = np.asarray(labels)
        print(labels.shape)
        model = Sequential()
        model.add(Dense(units=1298, input_dim=5, activation='relu'))
        model.add(Dense(2, activation='sigmoid'))
        model.compile(optimizer='rmsprop',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        history = model.fit(scaled[:51940], labels[:51940], validation_split=0.33, epochs=1000, batch_size=10)
        print(history.history.keys())
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.legend(['train', 'test'])
        plt.show()
        score = model.evaluate(scaled[51940:], labels[51940:], batch_size=10)
        print(score)
        import pdb; pdb.set_trace()

        return HttpResponse('ok')
