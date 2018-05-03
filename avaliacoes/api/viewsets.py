from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    """
        A viewset for viewing and editing user instances.
        """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer