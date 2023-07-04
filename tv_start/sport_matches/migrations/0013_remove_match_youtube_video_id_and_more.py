# Generated by Django 4.2 on 2023-05-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_matches', '0012_match_youtube_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='youtube_video_id',
        ),
        migrations.AddField(
            model_name='match',
            name='youtube_video_url',
            field=models.URLField(blank=True),
        ),
    ]
