from rest_framework import serializers
from .models import Director, Movie, Rating

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'birth_year']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    director_id = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(), source='director', write_only=True
    )
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year', 'director', 'director_id']

class RatingSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True
    )
    
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'movie_id', 'score', 'created_at']