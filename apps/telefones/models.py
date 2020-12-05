from django.db import models
import uuid
from apps.pessoas.models import Pessoa


TIPO_TELEFONE = [
    ('FIX', "Fixo"),
    ('CEL', "Celular"),
    ('WHP', "whatsapp"),
    ('OUT', "Outro"),
]


class Telefone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_telefone = models.CharField(max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    pessoa_telefone = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.CharField(max_length=32)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.telefone
