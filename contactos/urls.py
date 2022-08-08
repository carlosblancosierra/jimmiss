from django.urls import path

from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.home_page, name="home"),
    path('<str:contact_id>', views.detail_page, name="detail"),
]
