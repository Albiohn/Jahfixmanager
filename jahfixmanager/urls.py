from django.urls import path
from miApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('etapas/', views.etapas, name='etapas'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro_empleado, name='registro'),  
    path('reparacion-detalle/', views.reparacion_detalle, name='reparacion_detalle'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('cotizacionin/', views.cotizacionin, name='cotizacionin'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('condiciones/', views.condiciones_servicio, name='condiciones'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('notificacion/', views.notificacion, name='notificacion'),
    path('recuperar/', auth_views.PasswordResetView.as_view(template_name='miApp/password_reset.html'), name='password_reset'),
    path('recuperar/done/', auth_views.PasswordResetDoneView.as_view(template_name='miApp/password_reset_done.html'), name='password_reset_done'),
]
