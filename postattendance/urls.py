from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path("attendance",views.attendance,name="attendance"),
]
