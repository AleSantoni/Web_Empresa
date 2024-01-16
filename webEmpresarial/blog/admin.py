from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published',  'post_category')
    ordering = ('author', 'published')
    search_fields = ( 'title', 'content', 'author__username', 'category__name' )
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')

    def post_category(self, obj):
        return ", ".join([c.name for c in obj.category.all().order_by("name")])
    post_category.short_description = 'Categoria'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
