from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    titulo = forms.CharField(max_length=250)
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Artigo
        fields = ('titulo','conteudo','categoria','imagem','status')

