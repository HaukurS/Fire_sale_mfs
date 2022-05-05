from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/items
    path('', views.index, name="index"),
    path('<int:id>', views.get_item_by_id, name='item_details'),
    path('create_item', views.create_item, name='create_item'),
    path('delete_item<int:id>', views.delete_item, name='delete_item')
]