from django.urls import path
from .views import *

urlpatterns = [
    path('SignUp/',SignupView.as_view(),name="Sign Up"),
    path('SignIn/',SigninView.as_view(),name="Sign In"),
]