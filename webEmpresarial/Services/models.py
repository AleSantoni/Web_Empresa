from django.db import models

# Create your models here.
class Services(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo") # caracter de texto
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo") # caracter de texto
    content = models.TextField(verbose_name="Contenido") # texto largo
    image = models.ImageField( verbose_name="Imagen", upload_to="service") # imagen

    created= models.DateTimeField(auto_now_add=True,  verbose_name="Fecha de creacion")# fecha de creacion
    updated= models.DateTimeField(auto_now=True,  verbose_name="Fecha de edicion") # fecha de actualizacion

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created'] # ordenar por fecha de creacion de lo mas nuevo al viejo

    def __str__(self):
        return self.title
