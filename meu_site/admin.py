from django.contrib import admin

from meu_site.models import Artigo,Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','criado','publicado')
    list_filter = ('nome','criado','publicado')
    date_hierarchy = 'publicado'
    search_fields = ('nome',)

# admin.site.register(Artigo)
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado','status')

    # Cria campos de busca e define onde será procurado
    search_fields = ('titulo','conteudo')

    # Cria automaticamento o slug baseado no titulo
    prepopulated_fields = {'slug':('titulo',)}

    # Filtro
    list_filter = ('status','criado','publicado','autor')

    # Hieraquia de datas
    date_hierarchy = 'publicado'

    # lista de campos que você gostaria de mudar dentro de um widget input tanto para ForeignKey quanto ManyToManyField
    raw_id_fields = ('autor',)

    # Campos que só lemos
    readonly_fields = ("visualizar_imagem",)

    def visualizar_imagem(self,obj):
        return obj.view_imagem()
    visualizar_imagem.short_description = "Imagem Cadastrada"
