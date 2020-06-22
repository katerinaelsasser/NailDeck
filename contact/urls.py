from django.conf.urls import url
from .views import contact_us

urlpatterns = [
    url('contact/', contact_us, name='contact'),
]