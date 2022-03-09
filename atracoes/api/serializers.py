from rest_framework.serializers import ModelSerializer
from ..models import Atracao


class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao',
                  'horario_func', 'idade_minima']
