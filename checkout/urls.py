from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/checkout
    path('step_one/<int:id>', views.create_contactinfo, name='step_one'),
    path('step_two/<int:id>', views.create_paymentinfo, name='step_two'),
    path('review/<int:id>', views.review_checkout, name='review')
]
