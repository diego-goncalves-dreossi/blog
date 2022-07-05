from django.urls import path
from . import views

urlpatterns =[
    path('',views.BlogListView.as_view(),name='pagina_inicial'),
    path('sobre/',views.SobrePag.as_view(),name="sobre"),
    path('artigo/novo/',views.BlogCreateView.as_view(),name="novo_artigo"),
    path('artigo/<slug:slug>/',views.BlogDetailView.as_view(),name="artigo_detalhe"),
    path('artigo/<slug:slug>/editar',views.BlogUpdateView.as_view(),name='art_edit'),
    path('artigo/<slug:slug>/deletar', views.BlogDeleteView.as_view() ,name="deletar_art")
]

"""
artigo/novo precisa estar antes de artigo/<slug:slug> para não ocorrer
erros (palavra novo ser confundida com slug) 
"""
