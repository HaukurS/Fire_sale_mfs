from django.urls import path
from . import views

path('step_one', views.create_contactinfo, name='step_one')