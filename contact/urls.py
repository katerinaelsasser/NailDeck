from django.conf.urls import url, include
from .views import contact, contact_sent

urlpatterns = [
    url('contact/', contact, name='contact'),
    url('contact/sent', contact_sent, name='contact_sent')
]