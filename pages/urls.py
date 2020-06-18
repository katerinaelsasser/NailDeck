from django.conf.urls import url, include
from .views import about_view, terms_view, faq_view

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms-conditions/', terms_view, name="terms"),
    url('faq/', faq_view, name="faq"),
]