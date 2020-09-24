# Generated by Django 3.1.1 on 2020-09-24 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ManyToManyField(blank=True, null=True, related_name='ofertas', to='categorias.Categoria')),
                ('ofertante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofertas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha_subido', models.DateTimeField(auto_now_add=True)),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofertas.oferta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Imagen de Oferta',
                'verbose_name_plural': 'Imágenes de Oferta',
            },
        ),
    ]