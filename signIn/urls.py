from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/register
    path('register_user', views.register_user, name="register_user"),
]