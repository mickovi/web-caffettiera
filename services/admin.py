from django.contrib import admin
from .models import Service # Acceder a la app desde el panel del admin

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)