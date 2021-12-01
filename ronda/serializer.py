from rest_framework import serializers

from ronda.models import Cliente, Moto, Venda


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cnh', 'data_nasc']


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'


class ListaVendasClienteSerializer(serializers.ModelSerializer):
    moto = serializers.ReadOnlyField(source='moto.modelo')
    cliente = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Venda
        fields = ['id', 'nota_fiscal', 'moto', 'cliente']

