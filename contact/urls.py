from django.conf.urls import url, include
from .views import contact

urlpatterns = [
    url('contact/', contact, name='contact'),
]