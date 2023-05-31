from rest_framework import serializers
from .models import Cliente, Contato


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    contatos = ContatoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nome_completo",
            "email",
            "telefone",
            "data_registro",
            "contatos",
        ]
