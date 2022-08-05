from django.urls import path

from . import views

app_name = 'skus'

urlpatterns = [
    path('', views.all_page, name="all"),
    path('<str:division_code>', views.list_page, name="list"),
    path('detalle/<str:slug>', views.detail_page, name="detail"),
]
