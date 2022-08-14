from django.urls import path
from .views import vue

urlpatterns = [
    path('', vue),
]
