# Cria processadores de contexto, torna valores de determinado 
# model em dicionários que serão acessados de qualquer lugar do 
# sistema.
from .models import Link

def ctx_social(request):
    ctx_dict = {}
    links = Link.objects.all()

    for link in links:
        ctx_dict[link.chave] = link.url
    return ctx_dict