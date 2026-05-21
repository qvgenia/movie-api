from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, MovieViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]