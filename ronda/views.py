from rest_framework import viewsets, generics

from ronda.models import Cliente, Moto, Venda
from ronda.serializer import MotoSerializer, ClienteSerializer, VendaSerializer, ListaVendasClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class MotosViewSet(viewsets.ModelViewSet):
    """Exibindo todas as motos"""
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class VendasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as vendas"""
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class ListaVendaCliente(generics.ListAPIView):
    """Listando as Compras de um cliente"""

    def get_queryset(self):
        queryset = Venda.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVendasClienteSerializer
