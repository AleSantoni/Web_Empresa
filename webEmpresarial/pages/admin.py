from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin): # crea la vista de administracion de la pagina
    #readonly_fields = ('created','updated') # solo lectura de campos
    #list_display = ('title','order') # crea la vista con titulo y orden
    #search_fields = ('title',) # busca por titulo
    #date_hierarchy = 'created' # crea la vista con fecha de creacion
    #list_filter = ('title',) # filtra por titulo
    #save_on_top = True # guarda en la parte superior de la pagina
    #list_per_page = 10 # crea la vista con 10 registros por pagina
    #prepopulated_fields = {'slug':('title',)} # crea el slug automaticamente con el titulo de la pagina
    #ordering = ('order',) # ordena por orden de la pagina
    #fields = ('title','order','slug','content') # crea la vista con titulo, orden, slug, contenido
    #fieldsets = (
    readonly_fields = ('created','updated')
    list_display = ('title','order')# crea la vista con titulo y orden

admin.site.register( Page, PageAdmin) # registra la vista de administracion de la pagina