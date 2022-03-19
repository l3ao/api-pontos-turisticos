from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
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
        queryset_base = self.filter_queryset(self.get_queryset())
        if 'nome' in request.data:
            queryset = queryset_base.filter(nome__icontains=request.data['nome'])
        else:
            queryset = queryset_base.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'Ponto turistico denunciado': True})
    
    @action(methods=['get'], detail=False)
    def situacao(self, request, pk=None):
        return Response({'Situação dos pontos turisticos': 'OK'})
