"""web_caffettiera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    # Path del core
    path('', include('core.urls')),

    # Path de services
    path('services/', include('services.urls')),

    # Path del blog
    path('blog/', include('blog.urls')),

    # Path de pages
    path('page/', include('pages.urls')),

    # Path de contact
    path('contact/', include('contact.urls')),

    # Path del admin
    path('admin/', admin.site.urls),
]

# Servir archivos estáticos desde django
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Cambiar el título y subtítulo del admin
admin.site.site_header = 'La Caffetiera'
admin.site.index_title = 'Panel del Administrador'
admin.site.site_title = 'La Caffetiera'