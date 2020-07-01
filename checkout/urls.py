from django.conf.urls import url
from .views import checkout, confirmation

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url('confirmation', confirmation, name='confirmation'),

]