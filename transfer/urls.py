from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send/', views.send_file, name='send_file'),
    path('receive/', views.receive_file, name='receive_file'),
]
