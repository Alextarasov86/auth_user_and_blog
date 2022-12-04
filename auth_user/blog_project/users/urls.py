from django.urls import path
from .views import AuthView, VerifyView

urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('verify/', VerifyView.as_view()),

]