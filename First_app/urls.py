from . import views 
from django.urls import path

URL_PATTERN=[
    path('', views.home, name='home'),
]

