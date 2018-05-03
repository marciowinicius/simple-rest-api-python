from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracoesSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentariosSerializer
from core.models import PontoTuristico
from endereco.api.serializers import EnderecosSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecosSerializer(many=False)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2')

    def get_descricao_completa(self, obj):
        return obj.nome + ' ' + obj.descricao