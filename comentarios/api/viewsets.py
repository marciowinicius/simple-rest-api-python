from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from .serializers import ComentariosSerializer


class ComentarioViewSet(ModelViewSet):
    """
        A viewset for viewing and editing user instances.
        """
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer