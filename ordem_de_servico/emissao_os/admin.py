# admin.py

from django.contrib import admin
from .models import Loja, Servico, OrdemServico

admin.site.register(Loja)
admin.site.register(Servico)
admin.site.register(OrdemServico)
