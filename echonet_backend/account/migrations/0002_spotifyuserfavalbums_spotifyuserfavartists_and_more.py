# Generated by Django 5.2.1 on 2025-05-30 06:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyUserFavAlbums',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('album_id', models.CharField(blank=True, max_length=255, null=True)),
                ('album_name', models.CharField(blank=True, max_length=255, null=True)),
                ('album_artist', models.CharField(blank=True, max_length=255, null=True)),
                ('album_image', models.URLField(blank=True, null=True)),
                ('album_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spotifyuser_fav_albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyUserFavArtists',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artist_id', models.CharField(blank=True, max_length=255, null=True)),
                ('artist_name', models.CharField(blank=True, max_length=255, null=True)),
                ('artist_image', models.URLField(blank=True, null=True)),
                ('artist_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spotifyuser_fav_artists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyUserFavTracks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('track_id', models.CharField(blank=True, max_length=255, null=True)),
                ('track_name', models.CharField(blank=True, max_length=255, null=True)),
                ('track_artist', models.CharField(blank=True, max_length=255, null=True)),
                ('track_image', models.URLField(blank=True, null=True)),
                ('track_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spotifyuser_fav_tracks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
