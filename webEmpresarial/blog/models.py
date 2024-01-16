from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre") # caracter de texto

    created= models.DateTimeField(auto_now_add=True,  verbose_name="Fecha de creacion")# fecha de creacion
    updated= models.DateTimeField(auto_now=True,  verbose_name="Fecha de edicion") # fecha de actualizacion

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created'] # ordenar por fecha de creacion de lo mas nuevo al viejo

    def __str__(self):
        return self.name

class Post(models.Model):


    title = models.CharField(max_length=200, verbose_name="Titulo") # caracter de texto
    content = RichTextField(verbose_name="Contenido") # caracter de texto no tiene tamaño concreto
    published = models.DateTimeField(verbose_name="Fecha de Publicacion",default=timezone.now)  # Usar timezone.now sin ejecutar la función
    image = models.ImageField(upload_to="blog", verbose_name="Imagen", null=True, blank=True)  # imagen puede ser nulo
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor") # llave foranea
    category = models.ManyToManyField(Category, related_name="get_posts", verbose_name="Categoria") # llave foranea
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")  # fecha de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")  # fecha de actualizacion
    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created'] # ordenar por fecha de creacion de lo mas nuevo al viejo

    def __str__(self):
        return self.title

