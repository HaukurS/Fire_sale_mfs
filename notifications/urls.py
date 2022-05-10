from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/notifications
    path('', views.show_notifications, name='notifications')

]