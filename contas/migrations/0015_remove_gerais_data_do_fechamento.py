# Generated by Django 4.0.5 on 2023-02-17 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0014_gerais_data_do_fechamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerais',
            name='data_do_Fechamento',
        ),
    ]