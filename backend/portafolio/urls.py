from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portafolio' ),
    path('project/<id>', views.proyect, name='project')
    
]