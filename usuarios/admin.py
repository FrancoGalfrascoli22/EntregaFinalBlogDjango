from django.contrib import admin
from .models import PerfilUsuario

# Register your models here.

admin.site.register(PerfilUsuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
    )