from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^items/(?P<pk>\d+)$', views.ItemDetail.as_view(), name='item-detail')
]