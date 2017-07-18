from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.transaction_list, name='transaction_list'),
    url(r'^add/$', views.transaction_add, name='transaction_add')
]
