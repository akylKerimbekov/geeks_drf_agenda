from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=150)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name='movies', null=True)


STAR_CHOICES = [(i, str(i)) for i in range(1, 6)]


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, related_name='reviews', null=True)
    stars = models.IntegerField(choices=STAR_CHOICES, null=True)
