from rest_framework import serializers
from .models import Company, Denuncia

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [ 'id', 'name', 'cnpj', 'companyType', 'address' ]


class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = [ 'id', 'endereco', 'numero', 'bairro', 'cidade', 'descricao' ]