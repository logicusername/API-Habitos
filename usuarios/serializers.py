from rest_framework import serializers
from .models import Usuarios, Habitos, Seguimientos, Logros

class UsuarioSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','nombre','correo','contraseña', 'fecha_creado')
        read_only_fields = ('fecha_creado',)

class HabitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitos
        fields = ('id','nombre_habito','descripcion','categoria','frecuencia','prioridad','estado','fecha_inicio','usuario')
        

class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimientos
        fields = ('id','fecha','estado','nota','habito')

class LogrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logros
        fields = ('id_notificacion','mensaje','fecha_envio')
        