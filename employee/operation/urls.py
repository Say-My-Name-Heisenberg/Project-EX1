from django.urls import path
from .views import *

urlpatterns = [
    path ('add/',AddView.as_view()),
    path('sub/',SubView.as_view()),
    path('mul/',MulView.as_view()),
    path('div/',DivView.as_view()),
    path('CV/',CountView.as_view()),
]
