# Generated by Django 2.0.7 on 2018-07-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musictrack',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
