from django.urls import path
from . import views

urlpatterns = [
    path('Projects/', views.projects, name= 'Projects')
]