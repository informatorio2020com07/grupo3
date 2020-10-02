# Generated by Django 3.1.1 on 2020-09-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0006_auto_20200928_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='estado',
            field=models.CharField(choices=[('en espera', 'En espera'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado'), ('finalizado', 'Finalizado')], default='en espera', max_length=15),
        ),
    ]