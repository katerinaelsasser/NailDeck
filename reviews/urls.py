from django.conf.urls import url, include
from .views import review

urlpatterns = [
    url('review/', review, name="review"),
]