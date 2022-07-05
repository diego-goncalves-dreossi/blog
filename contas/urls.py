from django.urls import path,include
from . import views

urlpatterns = [
    path('cadastro/', views.CadastroView.as_view(), name='cadastro')
]


