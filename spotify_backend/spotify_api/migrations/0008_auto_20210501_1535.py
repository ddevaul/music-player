# Generated by Django 3.2 on 2021-05-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_api', '0007_auto_20210501_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='albumOrder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderedAlbumSong',
        ),
    ]
