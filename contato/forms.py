from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome",widget=forms.TextInput(attrs={'placeholder':'Digite seu nome...'}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder':'Digite seu email...'}))
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'placeholder':'Digite a Mensagem'}))
