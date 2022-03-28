from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # Contiene todos los usuarios en el panel del admin

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)
    updated =  models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(verbose_name='Nombre', max_length=50)
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to='blog', null=True, blank=True)
    ### Relaciones ###
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE) # models.CASCADE: borra todas las entradas cuando se elimina un autor
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts') # Cambiar el nombre post_set (default) para la consulta de relación inversa
    ##################
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)
    updated =  models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title