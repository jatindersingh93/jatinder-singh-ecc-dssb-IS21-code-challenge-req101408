"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url  
from django.urls import path, include
#from productApi.views import ProductViewSet
from rest_framework import routers
from productApi import views 
# router = routers.DefaultRouter()
# router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/products$', views.product_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail),
    #url(r'^api/products/published$', views.product_list_published)
]
