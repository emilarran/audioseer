from django.db import models
import numpy

# Create your models here.


class MusicTrack(models.Model):
    C = 0
    CS = 1
    D = 2
    DS = 3
    E = 4
    F = 5
    FS = 6
    G = 7
    GS = 8
    A = 9
    AS = 10
    B = 11
    KEY_CHOICES = (
        (C, 'C'),
        (CS, 'C#'),
        (D, 'D'),
        (DS, 'D#'),
        (E, 'E'),
        (F, 'F'),
        (FS, 'F#'),
        (G, 'G'),
        (GS, 'G#'),
        (A, 'A'),
        (AS, 'A#'),
        (B, 'B')
    )

    MINOR = 0
    MAJOR = 1
    MODE_CHOICES = (
        (MINOR, 'Minor'),
        (MAJOR, 'Major')
    )

    rank = models.PositiveSmallIntegerField(blank=True, null=True)
    track_id = models.CharField(max_length=80, blank=True, null=True)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    duration_ms = models.PositiveIntegerField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    instrumentalness = models.FloatField(blank=True, null=True)
    key = models.PositiveSmallIntegerField(
        choices=KEY_CHOICES, blank=True, null=True
    )
    loudness = models.FloatField(blank=True, null=True)
    liveness = models.FloatField(blank=True, null=True)
    mode = models.PositiveSmallIntegerField(
        choices=MODE_CHOICES, blank=True, null=True
    )
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    time_signature = models.PositiveSmallIntegerField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    streams = models.PositiveIntegerField(blank=True, null=True)

    @property
    def numpyArray(self):
        return numpy.array([
            self.duration_ms,
            self.key,
            self.mode,
            self.tempo,
            self.time_signature,
        ])

    @property
    def popularArray(self):
        return numpy.array([
            self.isPopular,
            self.isNotPopular
        ])

    @property
    def isPopular(self):
        return 1 if self.rank <= 100 else 0

    @property
    def isNotPopular(self):
        return 0 if self.rank <= 100 else 1    
