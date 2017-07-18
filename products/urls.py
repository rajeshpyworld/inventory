from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.productList, name='product_list'),
    url(r'^add/$', views.product_add, name='product_add'),
    url(r'^(?P<pk>\d+)/edit/$', views.product_update, name='product_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),

]
