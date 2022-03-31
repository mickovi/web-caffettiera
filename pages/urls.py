from django.urls import path
from . import views

# TODO: Evitar agregar cualquier cadenas de de page_id
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]