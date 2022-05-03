from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/User
    path('', views.index, name="index "),
]