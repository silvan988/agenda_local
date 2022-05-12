from django.contrib import admin
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email',
                    'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'categoria')
    list_editable = ('mostrar',)
    list_filter = ('categoria',)

admin.site.register(Contato, ContatoAdmin)
