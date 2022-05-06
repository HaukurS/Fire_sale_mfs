from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/register
    path('register_user', views.register_user, name="register_user"),
    path('login', LoginView.as_view(template_name='SignIn/Login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]