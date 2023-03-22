from django.urls import path
from . import views

urlpatterns = [
    path('resume12/', views.resume12, name='resume12'),
]