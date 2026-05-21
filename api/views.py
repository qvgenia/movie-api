from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Director, Movie, Rating
from .serializers import DirectorSerializer, MovieSerializer, RatingSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__icontains=name)
        return qs
    
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Director.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)

# Аналогично сделайте для MovieViewSet и RatingViewSet
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.query_params.get('title')
        director_id = self.request.query_params.get('director_id')
        if title:
            qs = qs.filter(title__icontains=title)
        if director_id:
            qs = qs.filter(director_id=director_id)
        return qs
    
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Movie.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            qs = qs.filter(movie_id=movie_id)
        return qs
    
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Rating.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)