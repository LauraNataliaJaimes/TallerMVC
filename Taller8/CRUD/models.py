from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.id

class TipoDocumento(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=3)
    Descripcion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.id

class Persona(models.Model):
    id=models.IntegerField(primary_key=True)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    idTipoDocumento=models.OneToOneField(TipoDocumento, on_delete=models.CASCADE)
    documento=models.CharField(max_length=10)
    lugarResidencia=models.OneToOneField(Ciudad, on_delete=models.CASCADE)
    fechaNacimiento=models.DateField()
    email=models.EmailField()
    telefono=models.CharField(max_length=8)
    usuario=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.id


# python manage.py shell
# Insertar Persona x consola: p1=Persona.objects.create(nombres='Natalia', apellidos='Jaimes', documento='1098821999')
# Modificar valor de Persona creada x consola: p1.Nombre='Laura Natalia' -saltodelinea- p1.save() 
# Eliminar objeto de Persona x consola: p1=Persona.objects.get(id=1) -saltodelinea- p1.delete()