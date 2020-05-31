from django.urls import path
from .views import about_view, terms_view, payments_view

urlpatterns = [
    path('about/', about_view, name="about"),
    path('terms-conditions/', terms_view, name="terms"),
    path('payments/', payments_view, name="payments")

]