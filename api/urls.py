from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, MovieViewSet, RatingViewSet, GenreViewSet, ActorViewSet

router = DefaultRouter()
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'actors', ActorViewSet, basename='actor')

urlpatterns = [
    path('', include(router.urls)),
]