from django.urls import path
from . import views

urlpatterns = [
    path('', views.surname),
    path('poem/', views.poem, name='poem'),
]