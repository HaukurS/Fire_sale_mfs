from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/checkout
    path('step_one', views.create_contactinfo, name='step_one'),
    path('step_two', views.create_paymentinfo, name='step_two')
]
