# Generated by Django 2.0.7 on 2018-07-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0002_musictrack_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='musictrack',
            name='streams',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
