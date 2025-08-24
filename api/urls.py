from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MovieViewSet, AlbumViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]