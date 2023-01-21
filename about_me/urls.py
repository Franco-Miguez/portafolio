from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.index, name="about-me"),
    
]