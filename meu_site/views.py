from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,UpdateView,DeleteView,TemplateView
from django.views.generic.edit import CreateView
from . models import Artigo
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ArtigoForm
from django.contrib.auth.mixins import LoginRequiredMixin
# ou from django.contrib.auth.decorators import login_required


class BlogListView(ListView):
    model = Artigo
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Artigo
    template_name = 'art_detalhe.html'
    context_object_name = 'art'
    

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Artigo
    template_name = 'novo_artigo.html'
    form_class = ArtigoForm
    success_message = "%(field)s criado com sucesso"

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Artigo
    form_class = ArtigoForm
    template_name = 'art_edit.html'
    success_message = "%(field)s alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Artigo
    template_name = 'art_delete.html'
    success_url = reverse_lazy('pagina_inicial')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request,*args,*kwargs)

class SobrePag(TemplateView):
    template_name = 'sobre.html'
