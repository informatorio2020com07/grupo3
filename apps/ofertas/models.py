import os

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from apps.categorias.models import Categoria


def get_image_path(instancia, filename):
    """Construye la ruta donde se van a guardar las imágenes de perfil"""
    oferta_id = instancia.id
    # if user_id is None:
    #     user_id = User.objects.order_by("id").last().id + 1
    path = os.path.join("img/ofertas/", str(oferta_id), "oferta", filename)
    return path


class ImagenOferta(models.Model):
    """Imágenes para las ofertas"""
    imagen = models.ImageField(default='img/ofertas/por_defecto/oferta-img.jpg', upload_to=get_image_path, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subido = models.DateTimeField(auto_now_add=True)
    oferta = models.ForeignKey('Oferta', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Imagen de Oferta'
        verbose_name_plural = 'Imágenes de Oferta'
    

class Oferta(models.Model):
    imagen_portada = models.ImageField(default='img/ofertas/por_defecto/oferta-img.jpg', upload_to=get_image_path, null=True, blank=True)
    ofertante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ofertas')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(default="Sin descripción", null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, null=True, blank=True, related_name='ofertas')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    imagenes = models.ManyToManyRel(to=ImagenOferta, field='oferta')

    def __str__(self):
        return self.titulo
