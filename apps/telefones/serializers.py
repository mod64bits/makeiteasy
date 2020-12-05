from rest_framework.serializers import ModelSerializer
from .models import Telefone


class TelefoneSerializer(ModelSerializer):
    class Meta:
        model = Telefone

        fields = ['id', 'tipo_telefone', 'pessoa_telefone', 'telefone', 'criado_em', 'modificado_em']




