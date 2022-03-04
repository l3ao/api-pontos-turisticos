from rest_framework.viewsets import ModelViewSet
from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
