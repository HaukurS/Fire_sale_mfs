from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/home
    path('', views.home, name="homepage"),
    path('search_item', views.search_item, name="itemsearch")
]
