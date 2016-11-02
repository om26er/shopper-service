from django.conf.urls import include, url
from django.contrib import admin

from shopper_app import urls as shopper_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(shopper_url)),
]
