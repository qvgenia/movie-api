from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    duration = models.IntegerField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.movie.title} - {self.score}'