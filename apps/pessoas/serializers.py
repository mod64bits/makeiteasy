from rest_framework.serializers import ModelSerializer
from .models import Pessoa


class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa

        fields = ['id', 'descricao', 'usuario', 'cpf_cnpj', 'tipo_pessoa', 'informacoes_adicionais', 'criado_em',
                  'modificado_em']




