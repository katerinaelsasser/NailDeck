from django.conf.urls import url, include
from .views import about_view, terms_view, social_view

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms/', terms_view, name="terms"),
    url('social/', social_view, name="social"),
]