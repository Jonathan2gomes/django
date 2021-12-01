from django.contrib import admin

from ronda.models import Cliente, Moto, Venda


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnh', 'data_nasc')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'id',)
    list_per_page = 5


admin.site.register(Cliente, Clientes)


class Motos(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'ano', 'preco', 'descricao')
    list_display_links = ('id', 'modelo')
    search_fields = ('id', 'modelo',)


admin.site.register(Moto, Motos)


class Vendas(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'moto', 'nota_fiscal')
    list_display_links = ('id',)
    search_fields = ('id',)


admin.site.register(Venda, Vendas)

