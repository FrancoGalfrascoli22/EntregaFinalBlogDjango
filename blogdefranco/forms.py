from dataclasses import field
from django import forms
from .models import Post, Comentarios, Contacto
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.db.models import Count

class PostForm(forms.ModelForm):

    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    epigrafe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-2'}))
    autor = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), widget=forms.Select(attrs={'class': 'form-control mb-2'}))
    fecha = forms.DateField(input_formats=['%m/%d/%Y'], label='Fecha', widget=DatePickerInput())
    imagen = forms.ImageField(label='Imagen (1920x1080)', widget=forms.FileInput(attrs={'class': 'form-control mb-2'}))
    cuerpo = forms.CharField(label='Cuerpo', widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('titulo', 'epigrafe', 'autor', 'fecha', 'imagen', 'cuerpo')
        
class EditForm(forms.ModelForm):
    
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    epigrafe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    fecha = forms.DateField(input_formats=['%m/%d/%Y'], label='Fecha', widget=DatePickerInput())
    imagen = forms.ImageField(label='Imagen (1920x1080)', widget=forms.FileInput(attrs={'class': 'form-control'}))
    cuerpo = forms.CharField(label='Cuerpo', widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('titulo', 'epigrafe', 'fecha', 'imagen', 'cuerpo')
        
class ComentarioForm(forms.ModelForm):
    
    #nombre = forms.MultipleChoiceField(widget=forms.Select(attrs={'class': 'form-control',}))
    cuerpo = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comentarios
        fields = ('cuerpo',)
        
class ContactoForm(forms.ModelForm):
    
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'telefono', 'mensaje')