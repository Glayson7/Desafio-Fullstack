from rest_framework import viewsets
from .models import Cliente, Contato
from .serializers import ClienteSerializer, ContatoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()


class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer

    def get_queryset(self):
        user = self.request.user
        cliente_pk = self.kwargs["cliente_pk"]
        return Contato.objects.filter(
            cliente__user=user, cliente_id=cliente_pk
        )
