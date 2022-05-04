from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.home_page, name="home"),
    # path('agregar', views.agregar_page),
]
