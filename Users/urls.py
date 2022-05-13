from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/User
    path('profile', views.show_profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile')
]