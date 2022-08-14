from django.urls import path
from .views import Drogasil

urlpatterns = [
    path('search', Drogasil.as_view()),
]
