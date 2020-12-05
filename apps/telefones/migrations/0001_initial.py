# Generated by Django 3.1.4 on 2020-12-05 00:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo_telefone', models.CharField(blank=True, choices=[('FIX', 'Fixo'), ('CEL', 'Celular'), ('WHP', 'whatsapp'), ('OUT', 'Outro')], max_length=8, null=True)),
                ('telefone', models.CharField(max_length=32)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('pessoa_telefone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa')),
            ],
        ),
    ]