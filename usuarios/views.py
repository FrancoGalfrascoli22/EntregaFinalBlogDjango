from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegistrarseForm, EditarPerfilUsuarioForm, EditarUserForm
from django.views.generic import DetailView, UpdateView
from .models import PerfilUsuario
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class Registrarse(generic.CreateView):
    form_class = RegistrarseForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class EditarPerfil(UpdateView):
    model = PerfilUsuario
    form_class = EditarPerfilUsuarioForm
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('Inicio')
    
    #def get_object(self):
        #return self.request.user
    
class CambiarContraseña(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/cambiar_contraseña.html'
    success_url = reverse_lazy('Contraseña Cambiada')
    
def ContraseñaCambiada(request):
    return render(request, 'registration/contraseña_cambiada.html')


class Perfil(DetailView):
    model = PerfilUsuario
    template_name = 'registration/perfil_pagina.html'
