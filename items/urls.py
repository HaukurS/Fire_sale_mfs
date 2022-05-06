from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/items
    path('filter_price_high', views.orderpricehigh, name="orderpricehigh"),
    path('filter_price_low', views.orderpricelow, name="orderpricelow"),
    path('', views.index, name="index"),
    path('<int:id>', views.get_item_by_id, name='item_details'),
    path('create_item', views.create_item, name='create_item'),
    path('delete_item<int:id>', views.delete_item, name='delete_item'),
    path('<str:category>', views.get_items_by_category, name='filter_items'),
    path('update_item/<int:id>', views.update_item, name='update_item'),
    path('place_bid', views.place_bid, name='place_bid')
]