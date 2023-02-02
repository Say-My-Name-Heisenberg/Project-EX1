from django.urls import path
from .views import *

urlpatterns = [
    path('log/',LogView.as_view(),name="Login"),
    path('reg/',RegView.as_view(),name="Registration"),
    path('staff/',StaffView.as_view(),name="Staff"),
]
