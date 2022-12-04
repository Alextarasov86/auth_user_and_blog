from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'comments', CommentsViewSet)
urlpatterns = [
    path('', include(router.urls)),
]