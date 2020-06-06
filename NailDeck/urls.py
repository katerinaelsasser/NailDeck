from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from pages import urls as urls_pages
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from pages.views import homepage
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name="homepage"),
    url(r'', include('pages.urls')),
    url(r'', include('accounts.urls')),
    url(r'', include('pages.urls')),
    url(r'products/', all_products, include('products.urls')),
    url(r'cart/', include('cart.urls')),
    url(r'search/', include('search.urls')),
    url(r'^media/(?P<url>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]