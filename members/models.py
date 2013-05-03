from django.db import models
from artists.models import Artist
# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=20, null=False)
    desc = models.TextField(null=False)
    email = models.CharField(max_length=50, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_member')