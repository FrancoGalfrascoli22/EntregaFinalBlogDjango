from django.urls import path
from . import views
from django.conf import settings
from .views import Registrarse, CambiarContraseña, Perfil, EditarPerfil
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('registrarse/', Registrarse.as_view(), name='Registrarse'),
    path('<int:pk>/editarperfil/', login_required(EditarPerfil.as_view(template_name="registration/editar_perfil.html")), name='Editar Perfil'),
    path('password/', CambiarContraseña.as_view(), name='Cambiar Contraseña'),
    path('password/realizado', views.ContraseñaCambiada, name='Contraseña Cambiada'),
    path('<int:pk>/perfil/', login_required(Perfil.as_view(template_name="registration/perfil_pagina.html")), name='Perfil'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
