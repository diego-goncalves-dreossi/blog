# Generated by Django 4.0.3 on 2022-04-06 16:34

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('meu_site', '0002_artigo_alterado_artigo_criado_artigo_publicado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigo',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AlterModelManagers(
            name='artigo',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
