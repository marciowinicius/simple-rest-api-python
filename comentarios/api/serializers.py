from rest_framework.serializers import ModelSerializer

from comentarios.models import Comentario


class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'comentario', 'usuario', 'data', 'aprovado')