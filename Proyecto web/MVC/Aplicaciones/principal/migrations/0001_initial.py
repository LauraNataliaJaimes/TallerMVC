# Generated by Django 3.1.7 on 2021-03-08 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=3)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=10)),
                ('fechaNacimiento', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=8)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('idTipoDocumento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='principal.tipodocumento')),
                ('lugarResidencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='principal.ciudad')),
            ],
        ),
    ]
