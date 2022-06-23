from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('contraseña/cambiar/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),

    path('contraseña/cambiar/completado/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('contraseña/reiniciar/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('contraseña/reiniciar/reiniciada/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('contraseña/reiniciar/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('contraseña/reiniciar/completado/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
