# Generated by Django 4.0.3 on 2022-06-27 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meu_site', '0004_alter_artigo_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='conteudo',
            field=models.TextField(verbose_name='Contéudo'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='titulo',
            field=models.CharField(max_length=250, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ManyToManyField(related_name='get_posts', to='meu_site.categoria'),
        ),
    ]
