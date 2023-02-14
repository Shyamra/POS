from django.db import models

# Create your models here.
class MovieList(models.Model):
    name = models.CharField(max_length=50)
    movie_time = models.CharField(max_length=50)
    rating = models.FloatField()
    typ = models.CharField(max_length=50)
    images = models.ImageField(upload_to='images/', default='images/None')
    def __str__(self):
        return self.name