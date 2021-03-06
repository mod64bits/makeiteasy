# Generated by Django 3.1.4 on 2020-12-05 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo_endereco', models.CharField(blank=True, choices=[('UNI', 'Único'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('COB', 'Cobrança'), ('ENT', 'Entrega'), ('OUT', 'Outro')], max_length=3, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=16, null=True)),
                ('bairro', models.CharField(blank=True, max_length=64, null=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('municipio', models.CharField(blank=True, max_length=64, null=True)),
                ('cep', models.CharField(blank=True, max_length=16, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('EX', 'EX'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], default='SP', max_length=3, null=True)),
                ('endereco_entrega', models.BooleanField(default=False, verbose_name='Endereço de Entrega')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
    ]
