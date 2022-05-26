from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('staff/home', views.staff_home_page, name="staff-home"),
]
