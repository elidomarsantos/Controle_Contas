# Generated by Django 4.0.5 on 2023-02-17 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0019_rename_data_do_fechamento_gerais_data_do_fechamento1'),
    ]

    operations = [
        migrations.AddField(
            model_name='gerais',
            name='data_do_Fechamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]