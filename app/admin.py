from django.contrib import admin
from .models import *
from django.contrib import admin 

admin.site.register(Cidade) 
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
# admin.site.register(Emprestimo)
# Register your models here.

class LivroInline(admin.TabularInline):
    model = Livro 
    extra = 1 
    
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',) 
    search_fields = ('nome',)
    inlines = [LivroInline]
    
admin.site.register(Livro)
admin.site.register(Autor,AutorAdmin)       
    
    