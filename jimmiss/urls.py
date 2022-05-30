"""jimmiss URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from accounts.views import login_page, register_page_local

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('nosotros', views.nosotros_page, name='nosotros'),
    path('cart', views.cart_page, name='cart'),
    path('producto', views.product_page, name='producto'),
    path('data', views.data_page, name='data'),
    path('create_tags', views.create_tags_page, name='create_tags'),
    path('sku_products', views.sku_products_page, name='sku_products'),


    path('division/caballero', views.division_page, name='caballero'),
    path('skus/', include('skus.urls')),
    path('carrito/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('addresses/', include('addresses.urls')),

    path('logout', LogoutView.as_view(), name='logout'),
    path('login', login_page, name="loging"),
    path('register-local', register_page_local, name="register-local"),

    path('admin/', admin.site.urls),
]

if settings.STATIC_LOCAL:
    # test mode
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
