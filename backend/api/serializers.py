from rest_framework import serializers
from .models import Company, Denuncia, Cadastro, PontosDeColeta


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'cnpj', 'companyType', 'address']


class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = ['id', 'endereco', 'numero', 'bairro', 'cidade', 'descricao']


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'nome', 'email', 'senha', 'confirmacaoSenha']

class PontosDeColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontosDeColeta
        fields = ['id', 'nome', 'telefone', 'endereco', 'materialColeta','tipoMaterial']
