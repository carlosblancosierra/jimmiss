from django.urls import path

from . import views

app_name = 'skus'

urlpatterns = [

    path('<str:slug>', views.detail_page, name="detail"),
]
