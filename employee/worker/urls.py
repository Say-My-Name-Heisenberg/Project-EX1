from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Homeview.as_view()),
    path('index/',index),
    
]
