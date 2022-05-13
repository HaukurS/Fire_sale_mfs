from django.urls import path
from . import views

# urlpatterns that connect to the notifications
urlpatterns = [
    # localhost:8000/notifications
    path('delete/<int:id>', views.delete_notification, name='delete'),
    path('', views.show_notifications, name='notifications')
]