from django.contrib import admin
from .models import Post, Comentarios, Contacto

# Register your models here.

admin.site.register(Post)
admin.site.register(Comentarios)
admin.site.register(Contacto)