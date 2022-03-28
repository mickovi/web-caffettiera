from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=50)
    url = models.URLField(verbose_name='Enlace', max_length=50, null=True, blank=True)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)
    updated =  models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name