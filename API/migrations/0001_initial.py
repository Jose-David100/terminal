# Generated by Django 3.0.7 on 2021-11-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del destino')),
                ('image', models.ImageField(upload_to='destinos_img/')),
                ('description', models.TextField(verbose_name='Descripcion del Destino')),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la Empresa')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_empresas/')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='contacto de la Empresa')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email de la Empresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Publicidad')),
                ('image', models.ImageField(upload_to='img_publicidad/')),
            ],
            options={
                'verbose_name': 'Publicidad',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DestinosTuristicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinos', models.ManyToManyField(to='API.Destino', verbose_name='Seleccione los destinos')),
            ],
            options={
                'verbose_name': 'Destino Turistico',
                'verbose_name_plural': 'Destinos Turisticos',
                'ordering': ['id'],
            },
        ),
    ]
