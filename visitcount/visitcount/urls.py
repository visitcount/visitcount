from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ItemList.as_view(), name='item-list'),
    url(r'^items/(?P<pk>\d+)$', views.ItemDetail.as_view(), name='item-detail'),
]