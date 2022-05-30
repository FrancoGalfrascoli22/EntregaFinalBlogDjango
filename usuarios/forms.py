from email.policy import default
from tkinter import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import EmailValidator, validate_email
from .models import PerfilUsuario
from ckeditor.widgets import CKEditorWidget

class RegistrarseForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2' )
    
    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["gmail.com", "yahoo.com", "hotmail.com",]
        if domain not in domain_list:
            raise forms.ValidationError("Por favor ingresa un mail con un dominio válido (gmail.com , yahoo.com , hotmail.com)")
        return data

#class EditarPerfilForm(forms.ModelForm):

    #first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}))
   # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #biografia = forms.CharField(label='Biografia', widget=forms.Textarea(attrs={'class': 'form-control'}))
    #avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    #class Meta:
       # model = PerfilUsuario
        #fields = ('biografia', 'avatar')
class EditarUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditarPerfilUsuarioForm(forms.ModelForm):
    biografia = forms.CharField(label='Biografia',widget=forms.Textarea(attrs={'class': 'form-control', 'maxlength': 600, 'cols': 30}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = PerfilUsuario
        fields = ('biografia', 'avatar')