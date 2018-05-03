from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from .serializers import EnderecosSerializer


class EnderecoViewSet(ModelViewSet):
    """
        A viewset for viewing and editing user instances.
        """
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer