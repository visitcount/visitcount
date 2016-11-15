from django.conf.urls import url, include
from django.contrib import admin


import visitcount.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(visitcount.urls)),
]
