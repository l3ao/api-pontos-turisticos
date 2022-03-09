from rest_framework.viewsets import ModelViewSet
from ..models import Atracao
from .serializers import AtracoesSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
