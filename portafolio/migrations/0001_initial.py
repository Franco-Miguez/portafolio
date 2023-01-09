# Generated by Django 4.1.4 on 2023-01-08 07:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Lenguaje')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('resume', models.CharField(max_length=150, verbose_name='Resumen')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='proyects/image', verbose_name='Imagen')),
                ('link', models.URLField()),
                ('languages', models.ManyToManyField(blank=True, null=True, to='portafolio.language', verbose_name='Lenguajes')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
