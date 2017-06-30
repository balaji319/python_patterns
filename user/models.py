from django.db import models
from django.core.urlresolvers import reverse

class Movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    is_favorite=models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.actor + '>>>'+self.actor_movie


class Song(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=50)
    song_name = models.CharField(max_length=30)
    def __str__(self):
        return self.file_type