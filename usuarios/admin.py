from django.contrib import admin
from .models import Usuarios, Habitos, Seguimientos, Logros

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Habitos)
admin.site.register(Seguimientos)
admin.site.register(Logros)