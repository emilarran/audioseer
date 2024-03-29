# Generated by Django 2.0.7 on 2018-07-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('track_id', models.CharField(blank=True, max_length=80, null=True)),
                ('acousticneses', models.FloatField(blank=True, null=True)),
                ('danceability', models.FloatField(blank=True, null=True)),
                ('duration_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('energy', models.FloatField(blank=True, null=True)),
                ('instrumentalness', models.FloatField(blank=True, null=True)),
                ('key', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('loudness', models.FloatField(blank=True, null=True)),
                ('mode', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('speechiness', models.FloatField(blank=True, null=True)),
                ('tempo', models.FloatField(blank=True, null=True)),
                ('time_signature', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valence', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
