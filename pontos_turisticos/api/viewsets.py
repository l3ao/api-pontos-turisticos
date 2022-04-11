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
        pk = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao')
        
        query_set = PontoTuristico.objects.all()
        
        if pk:
            query_set = query_set.filter(pk=pk)
            
        if nome:
            query_set = query_set.filter(nome__iexact=nome)
        
        if descricao:
            query_set = query_set.filter(descricao__iexact=descricao)
        
        return query_set
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

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
