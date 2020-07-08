from django.conf.urls import url, include
from .views import all_products, polish_category, care_category

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'polish', polish_category, name='polish_category'),
    url(r'care', care_category, name='care_category'),
]