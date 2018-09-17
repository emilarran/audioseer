from django.shortcuts import render
from preprocessing.models import MusicTrack
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from django.views import View
from django.http import HttpResponse
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import metrics
import random
import matplotlib.pyplot as plt
import numpy as np
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
            """
            This function prints and plots the confusion matrix.
            Normalization can be applied by setting `normalize=True`.
            """
            if normalize:
                cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
                print("Normalized confusion matrix")
            else:
                print('Confusion matrix, without normalization')

            print(cm)

            plt.imshow(cm, interpolation='nearest', cmap=cmap)
            plt.title(title)
            plt.colorbar()
            tick_marks = np.arange(len(classes))
            plt.xticks(tick_marks, classes, rotation=45)
            plt.yticks(tick_marks, classes)

            fmt = '.2f' if normalize else 'd'
            thresh = cm.max() / 2.
            for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
                plt.text(j, i, format(cm[i, j], fmt),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")

            plt.tight_layout()
            plt.ylabel('True label')
            plt.xlabel('Predicted label')
            plt.show()


class TrainingView(View):
    def get(self, request, *args, **kwargs):
        scaler = MinMaxScaler(feature_range=(0, 1))
        trackdata = [track.numpyArray for track in MusicTrack.objects.all()]
        random.shuffle(trackdata)
        toscale = []
        labels = []
        for track in trackdata:
            toscale.insert(
                len(toscale),
                [track[0], track[1], track[2], track[3], track[4], #, track[5], track[6]])#, track[7]])
                track[5], track[6], track[7], track[8], track[9]])
            labels.insert(len(labels), [track[10]])  # , track[11]])

        scaled = scaler.fit_transform(toscale)
        labels = np.array(labels)
        print(labels.shape)
        model = Sequential()
        model.add(Dense(units=64, input_dim=10, activation='relu'))
        model.add(Dense(units=32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam',
                      loss='logcosh',
                      metrics=['accuracy'])
        model.summary()
        # With logcosh = 0.05 loss with 84-85% accuracy
        # Wtih binary_crossentropy = 0.35 loss with 83-84% accuracy

        X_train, X_test, y_train, y_test = train_test_split(scaled, labels, test_size=0.33, random_state=0)


        history = model.fit(
            X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32, verbose=2, shuffle=True)

        scores = model.evaluate(X_train, y_train)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
        # Plotting train/test graph
        # print(history.history.keys())
        # plt.plot(history.history['loss'])
        # plt.plot(history.history['val_loss'])
        # plt.legend(['train', 'test'])
        # plt.show()
        rounded_predictions = model.predict_classes(X_test, batch_size=10, verbose=0)
        # Plotting confusion matrix
        cm = confusion_matrix(y_test, rounded_predictions)
        cm_plot_labels = ['Popular', 'Not_Popular']
        plot_confusion_matrix(cm, cm_plot_labels, title='Confusion Matrix')


        import pdb; pdb.set_trace()

        return HttpResponse('ok')
