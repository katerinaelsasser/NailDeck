from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from pages import urls as urls_pages
from cart import urls as urls_cart
from reviews import urls as urls_reviews
from contact import urls as urls_contact
from checkout import urls as urls_checkout
from pages.views import homepage
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name="homepage"),
    url(r'pages/', include(urls_pages)),
    url(r'accounts/', include(urls_accounts)),
    url(r'reviews/', include(urls_reviews)),
    url(r'contact/', include(urls_contact)),
    url(r'products/', include(urls_products)),
    url(r'cart/', include(urls_cart)),
    url(r'checkout/', include(urls_checkout)),
    url(r'^media/(?P<url>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]