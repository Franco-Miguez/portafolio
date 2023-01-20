from django.db import models
from ckeditor.fields import RichTextField
import portafolio.models

# Create your models here.
class Work(models.Model):
    company = models.CharField(verbose_name="compañia", max_length=150)
    job = models.CharField(verbose_name="Puesto", max_length=150)
    description = RichTextField(verbose_name="Descripción")
    start_work = models.DateField(verbose_name="Desde")
    end_work = models.DateField(verbose_name="Hasta", null=True)
    
    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"
    
    def __str__(self) -> str:
        return f"{self.company} | {self.job}"

class Course(models.Model):
    name = models.CharField(verbose_name="Curso", max_length=150)
    languages = models.ManyToManyField(portafolio.models.Language, verbose_name="Lenguajes", null=True, blank=True)
    description = RichTextField(verbose_name="Descripción")
    start_course = models.DateField(verbose_name="Desde")
    end_course = models.DateField(verbose_name="Hasta", null=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
    def __str__(self) -> str:
        return self.name
    
class Info(models.Model):
    name = models.CharField(verbose_name="Nombre completo", max_length=20)
    image_front = models.ImageField(validators="Imagen perfil", upload_to="media/image")
    image_logo = models.ImageField(validators="Imagen Logo", upload_to="media/image")
    job = models.CharField(verbose_name="Puesto", max_length=200)
    linkedin_link = models.URLField(verbose_name="Link Linkedin")
    linkedin_name = models.CharField(verbose_name="Nombre linkedin", max_length=50)
    github_link = models.URLField(verbose_name="Link Github")
    github_name = models.CharField(verbose_name="Nombre Github", max_length=50)
    youtube_link = models.URLField(verbose_name="Link Youtube")
    youtube_name = models.CharField(verbose_name="Nombre Youtube", max_length=50)
    web_link = models.URLField(verbose_name="Link Sitio Web")
    web_name = models.CharField(verbose_name="Nombre Sitio Web", max_length=50)
    update = models.DateField(verbose_name="Actualizado")
    email = models.EmailField(verbose_name="Email Contacto")
    
    