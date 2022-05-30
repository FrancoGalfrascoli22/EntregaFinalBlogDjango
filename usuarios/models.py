from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    biografia = models.TextField(max_length=600, default='No hay nada por aquí...')
    avatar = models.ImageField(default='avatar/default.jpg', upload_to='avatar', null=True)
    
    def __str__(self):
        return str(self.usuario)
    
    def get_first_name(self):
        global usuario
        return usuario.first_name
    
User._meta.get_field('email')._unique = True