from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create', views.create_page, name="create"),
    # path('confirm', views.delete_entry_page, name="delete-entry"),

]
