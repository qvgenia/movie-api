from rest_framework import serializers
from .models import Director, Movie, Rating, Genre, Actor

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'birth_year']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birth_year', 'country']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    director_id = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(), source='director', write_only=True
    )
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genres', write_only=True, many=True
    )
    actors = ActorSerializer(many=True, read_only=True)
    actor_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), source='actors', write_only=True, many=True
    )

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'year', 'duration',
            'director', 'director_id', 'genres', 'genre_ids', 'actors', 'actor_ids'
        ]

class RatingSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True
    )

    class Meta:
        model = Rating
        fields = ['id', 'movie', 'movie_id', 'score', 'created_at']