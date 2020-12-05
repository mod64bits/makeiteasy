from rest_framework.serializers import ModelSerializer
from .models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco

        fields = ['id', 'pessoa_padrao', 'tipo_endereco', 'logradouro', 'numero', 'complemento', 'municipio', 'cep',
                  'uf', 'endereco_entrega', 'criado_em', 'modificado_em']




