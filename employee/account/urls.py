from django.urls import path
from .views import *

urlpatterns = [
    path('log/',LogView.as_view(),name="Login"),
    path('reg/',RegView.as_view(),name="Registration"),
    path('staff/',StaffView.as_view(),name="Staff"),
    path('Delstaff/<int:sid>',StaffDelete.as_view(),name="DelStaff"),
    path('EditStaff/<int:sid>',StaffEdit.as_view(),name="EditStaff")
]
