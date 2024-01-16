from django.db import models

# Create your models here.
class Links(models.Model):
   key=models.SlugField(verbose_name= "Nombre clave" ,max_length=100,unique=True)
   name= models.CharField(verbose_name="Red Social",max_length=200)
   url= models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
   created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")  # fecha de creacion
   updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")  # fecha de actualizacion

   class Meta:
      verbose_name = 'enlace'
      verbose_name_plural = 'enlaces'
      ordering = ['name']  # ordenar por fecha de creacion de lo mas nuevo al viejo

   def __str__(self):
      return self.name
