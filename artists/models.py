from django.db import models

# Create your models here.

class Artist(models.Model):
    artistId = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=30, null=False)
    desc = models.TextField(null=True)
    role = models.PositiveSmallIntegerField(default=1, null=False)

class Member(models.Model):
    name = models.CharField(max_length=20, null=False)
    desc = models.TextField(null=True)
    email = models.CharField(max_length=50, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Video(models.Model):
    url = models.CharField(max_length=200, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Image(models.Model):
    filename = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Music(models.Model):
    filename = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)