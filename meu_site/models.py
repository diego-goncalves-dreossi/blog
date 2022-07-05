from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

# Manager personalizado
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-criado']


# Manager personalizado
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')



class Artigo(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado')
    )
    titulo = models.CharField(verbose_name='Título', max_length=250)
    slug = models.CharField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categoria = models.ManyToManyField(Categoria,related_name='get_posts')
    imagem = models.ImageField(upload_to='blog',blank=True,null=True)
    conteudo = RichTextField(verbose_name='Contéudo')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True) 
    # Configurado apenas na criação
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default='rascunho')

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse("artigo_detalhe", args=[self.slug])
    
    def get_absolute_url_update(self):
        return reverse("art_edit", args=[self.slug])
    # Faz com que o nome do registro no banco de dados seja mostrado com o nome do titulo
    def __str__(self):
        return f"{str(self.id)} - {self.titulo}"
    def view_imagem(self):
        return mark_safe(f'<img src={self.imagem.url} width="400px />"')
        view_image.short_description = "Imagem cadastrada"
        view_image.allow_tags = True
        
    class Meta:
        ordering = ('-publicado',)

    

@receiver(post_save,sender=Artigo)
def insert_slug(sender,instance,**kwargs):
    if kwargs.get('criado',False):
        print('Criando slug')
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()
