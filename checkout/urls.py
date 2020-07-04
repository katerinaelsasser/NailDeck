from django.conf.urls import url
from .views import checkout, confirmation

urlpatterns = [
    url('checkout/', checkout, name="checkout"),
    url('confirmation/', confirmation, name="confirmation"),

]