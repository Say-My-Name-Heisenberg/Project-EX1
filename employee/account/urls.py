from django.urls import path
from .views import *

urlpatterns = [
    path('log/',LogView.as_view()),
    path('reg/',RegView.as_view()),
]
