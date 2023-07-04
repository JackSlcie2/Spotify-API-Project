from rest_framework import serializers
from .models import Pacitentes

class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacitentes
        fields = ('cpf', 'rg', 'data', 'genero', 'cidade', 'telefone2', 'telefone', 'tipo', 'nome', 'medico', 'obsmed', 'como', 'bairro', 'rua', 'numero', 'complemento')