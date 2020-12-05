from django.db import models
import uuid

from apps.usuarios.models import User


TIPO_PESSOA = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]


class Pessoa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField('Descrição', max_length=50, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_padrao', null=True,
                                   blank=True, )
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=30, null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=2, choices=TIPO_PESSOA, default='PF')
    informacoes_adicionais = models.TextField('Informações adicionais', null=True, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __unicode__(self):
        s = self.descricao
        return s

    def __str__(self):
        s = self.descricao
        return s



