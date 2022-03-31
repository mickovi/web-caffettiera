from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Evaluamos los permisos de un grupo en tiempo de ejecución
    def get_readonly_fields(self, request, obj=None):
        # Sobreescribimos campos
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)