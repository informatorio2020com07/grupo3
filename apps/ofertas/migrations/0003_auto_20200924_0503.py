# Generated by Django 3.1.1 on 2020-09-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0002_oferta_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='descripcion',
            field=models.TextField(blank=True, default='Sin descripción', null=True),
        ),
    ]