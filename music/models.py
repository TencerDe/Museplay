from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return f"{self.title}-{self.artist}"
    
class UserProfile(AbstractUser):
    pass
