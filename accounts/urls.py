from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('home', views.home_page, name="home"),
    path('staff/home', views.staff_home_page, name="staff-home"),
    path('<str:username>', views.detail_page, name="detail"),
]
