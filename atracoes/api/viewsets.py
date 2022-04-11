from rest_framework.viewsets import ModelViewSet
from ..models import Atracao
from .serializers import AtracoesSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filterset_fields = ['nome', 'descricao']
