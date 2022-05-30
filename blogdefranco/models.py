from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length= 500)
    epigrafe = models.TextField(max_length=700)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(blank=False)
    imagen = models.ImageField(upload_to='post')
    cuerpo = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.autor) + ' --- ' + self.titulo + ' --- ' + str (self.fecha)
    
    def get_absolute_url(self):
        return reverse('Inicio')
    
class Comentarios(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.post) + ' --- ' + str (self.nombre)

class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    email = models.EmailField(max_length=200, unique=True)
    telefono = models.CharField(max_length=18)
    mensaje = models.TextField(max_length=350)
    
    def __str__(self):
        return str(self.email) + ' --- ' + str (self.telefono)