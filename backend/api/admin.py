from django.contrib import admin
from .models import Company, PontosDeColeta, Denuncia, Cadastro

admin.site.register(Company)
admin.site.register(Denuncia)
admin.site.register(Cadastro)
admin.site.register(PontosDeColeta)