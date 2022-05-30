from django.urls import path
from . import views
from .views import AllPosts, Lista, Archivo, CrearPost, EditarPost, BorrarPost, AñadirComentario, Contacto, contacto_realizado, acerca_de
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('', views.inicio, name='Inicio' ),
    path('', Lista.as_view(), name='Inicio' ),
    path('allposts/', AllPosts.as_view(), name='All Posts' ),
    path('archivo/<int:pk>', Archivo.as_view(), name='Archivo' ),
    path('crearpost/', login_required(CrearPost.as_view(template_name="blogdefranco/crud/crear_post.html")), name='Crear Post' ),
    path('editarpost/<int:pk>', login_required(EditarPost.as_view(template_name="blogdefranco/crud/editar_post.html")), name='Editar Post' ),
    path('borrarpost/<int:pk>', login_required(BorrarPost.as_view(template_name="blogdefranco/crud/borrar_post.html")), name='Borrar Post' ),
    path('archivo/<int:pk>/comentario/', login_required(AñadirComentario.as_view(template_name="blogdefranco/añadir_comentario.html")), name='Añadir Comentario' ),
    path('contacto/', Contacto.as_view(), name='Contacto'),
    path('contacto/realizado', views.contacto_realizado, name='Contacto Realizado'),
    path('sobre_mi/', views.acerca_de, name='Sobre Mi'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
