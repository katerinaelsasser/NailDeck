from django.conf.urls import url, include
from .views import about_view, terms_view, social_view, views.contact, views.success

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms/', terms_view, name="terms"),
    url('contact/', views.contact, name='contact'),
    url('contact/success/', views.success, name='success'),
    url('social/', social_view, name="social"),
]