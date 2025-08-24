from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.artist}"