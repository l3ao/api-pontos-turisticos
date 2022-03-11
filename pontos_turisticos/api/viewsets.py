from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        return Response({'test': 123})

    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})
