from django.db import models

class Ciudad(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)

class TipoDocumento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=3)
    Descripcion=models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)

# Create your models here.
class Persona(models.Model):
    id=models.AutoField(primary_key = True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    idTipoDocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento=models.CharField(max_length=10)
    lugarResidencia=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechaNacimiento=models.CharField(max_length=10)
    email=models.EmailField(max_length=200)
    telefono=models.CharField(max_length=8)
    usuario=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
