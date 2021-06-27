# Generated by Django 3.2 on 2021-05-01 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_api', '0006_auto_20210501_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedalbumsong',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spotify_api.album'),
            preserve_default=False,
        ),
    ]
