from django import template
from pages.models import Page

register = template.Library() # Se registra en la librería de templates

# Decorador que implementa una nueva funcionalidad: 
# convierte la función en un simple_tag
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
