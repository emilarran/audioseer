# Generated by Django 2.0.7 on 2018-07-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0003_musictrack_streams'),
    ]

    operations = [
        migrations.AddField(
            model_name='musictrack',
            name='liveness',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
