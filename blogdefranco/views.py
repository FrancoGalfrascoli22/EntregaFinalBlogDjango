from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Comentarios, Post, Contacto
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .forms import PostForm, EditForm, ComentarioForm, ContactoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#def inicio(request):
    #return render(request, 'blogdefranco/inicio.html')


class Lista(ListView):
    model = Post
    template_name = 'blogdefranco/inicio.html'
    ordering = ('-fecha', '-id')

class AllPosts(ListView):
    model = Post
    template_name = 'blogdefranco/archivo.html'
    ordering = ('-fecha', '-id')

class Archivo(DetailView):
    model = Post
    template_name = 'blogdefranco/crud/archivo_details.html'

class CrearPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogdefranco/crud/crear_post.html'
    
class Contacto(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'blogdefranco/contacto.html'
    success_url = reverse_lazy('Contacto Realizado')

def contacto_realizado(request):
    return render(request, 'blogdefranco/contacto_realizado.html')
    
class AñadirComentario(CreateView):
    model = Comentarios
    form_class = ComentarioForm
    template_name = 'blogdefranco/añadir_comentario.html'
    success_url = '/archivo/{post_id}'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.nombre = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class EditarPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blogdefranco/crud/editar_post.html'
    #fields = ['titulo', 'epigrafe', 'cuerpo', 'imagen']

class BorrarPost(DeleteView):
    model = Post
    template_name = 'blogdefranco/crud/borrar_post.html'
    success_url = reverse_lazy('Inicio')

def acerca_de(request):
    return render(request, 'blogdefranco/acerca_de.html')