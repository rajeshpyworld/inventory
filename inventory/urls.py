"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core.views import signup,customerList,home,customer_add,customer_update,customer_delete

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$',signup, name='signup'),
    url(r'^customers/$', customerList, name='customers'),
    url(r'^customer/add/$',customer_add, name='customer_add'),
    url(r'^customer/(?P<pk>\d+)/edit/$',customer_update, name='customer_update'),
    url(r'^customer/(?P<pk>\d+)/delete/$', customer_delete, name='customer_delete'),
    url(r'^product/', include("products.urls", namespace='products')),
    url(r'^transaction/', include("transactions.urls", namespace='transactions')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
