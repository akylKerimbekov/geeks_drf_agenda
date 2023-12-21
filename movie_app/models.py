from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
