from django.urls import path
from .views import *

urlpatterns = [
    path ('add/',AddView.as_view(),name="Addition"),
    path('sub/',SubView.as_view(),name="Substraction"),
    path('mul/',MulView.as_view(),name="Multiplication"),
    path('div/',DivView.as_view(),name="Division"),
    path('CV/',CountView.as_view()),
]
