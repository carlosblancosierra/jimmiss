from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('direccion', views.address_page, name="address"),
    # path('confirm', views.delete_entry_page, name="delete-entry"),

]
