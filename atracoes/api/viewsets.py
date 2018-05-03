from rest_framework.viewsets import ModelViewSet

from atracoes.models import Atracao
from .serializers import AtracoesSerializer


class AtracaoViewSet(ModelViewSet):
    """
        A viewset for viewing and editing user instances.
        """
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_fields = ('nome', 'descricao')