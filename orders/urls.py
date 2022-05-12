from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('address', views.address_page, name="address"),
    path('confirmar', views.confirm_page, name="confirm"),
    path('created', views.created_page, name="created"),

]
