from django.urls import path

from . import views

app_name = 'skus'

urlpatterns = [
    path('', views.list_page, name="list"),
    path('dama', views.dama_page, name="dama"),
    path('caballero', views.caballero_page, name="caballero"),
    path('niñas', views.ninas_page, name="niñas"),
    path('niños', views.ninos_page, name="niños"),
    path('preescolar', views.preescolar_page, name="preescolar"),
    path('bebe', views.bebe_page, name="bebe"),

    path('<str:slug>', views.detail_page, name="detail"),
]
