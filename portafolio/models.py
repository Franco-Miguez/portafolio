from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Language(models.Model):
    name = models.CharField(verbose_name="Lenguaje", max_length=50)
    
    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"
    
    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50)
    resume = models.CharField(verbose_name="Resumen", max_length=150)
    description = RichTextField(verbose_name="Descripción")
    languages = models.ManyToManyField(Language, verbose_name="Lenguajes", blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to='media/image')
    link_github = models.URLField(verbose_name="Link GitHub")
    
    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
    
    def __str__(self) -> str:
        return self.name
    