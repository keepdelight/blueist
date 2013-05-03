from django.db import models
from artists.models import Artist

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=200, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Image(models.Model):
    filename = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Music(models.Model):
    filename = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
