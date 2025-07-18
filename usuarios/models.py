from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.TextField()
    contraseña = models.CharField(max_length=200)
    fecha_creado = models.DateTimeField(auto_now_add=True)

class Habitos(models.Model):
    nombre_habito = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=200)
    prioridad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField(null=True)

    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Seguimientos(models.Model):
    fecha = models.DateTimeField(null=True)
    estado = models.CharField(max_length=200)
    nota = models.CharField(max_length=200)

    habito = models.ForeignKey(Habitos, on_delete=models.CASCADE)    

class Logros(models.Model):
    id_notificacion = models.CharField(max_length=200, primary_key=True)
    mensaje = models.TextField(blank=True)
    fecha_envio = models.DateTimeField(null=True)

    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)   