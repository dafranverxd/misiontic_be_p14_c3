from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Soporte, PQR

# Register your models here.

admin.site.register(Soporte)
admin.site.register(PQR)
