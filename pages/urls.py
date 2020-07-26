from django.conf.urls import url, include
from .views import about_view, terms_view, social_view, contact

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms/', terms_view, name="terms"),
    url('contact/', contact, name='contact'),
    url('social/', social_view, name="social"),
]