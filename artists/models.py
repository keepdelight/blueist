from django.db import models

# Create your models here.

class Artist(models.Model):
    artistId = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=30, null=False)
    desc = models.TextField(null=False)
    role = models.PositiveSmallIntegerField(default=1, null=False)
    # 1 : user, 2 : admin
