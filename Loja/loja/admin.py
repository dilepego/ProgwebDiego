from django.contrib import admin
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    search_fields =("Fabricante",)
class CategoriaAdmin(admin.ModelAdmin):    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    search_fields =("Categoria",)
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ("Produto",)
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao',
'preco', 'categoria',)
    empty_value_display = 'Vazio'
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)