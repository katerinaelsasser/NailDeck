from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('pages.urls')),

    url(r'^$', all_products, name='home'),
    url('', include('accounts.urls')),
    url('products/', include('products.urls')),
    url('cart/', include('cart.urls')),
    url('search/', include('search.urls')),
    url(r'^media/(?P<url>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]