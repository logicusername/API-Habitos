from rest_framework import viewsets, permissions
from usuarios.models import Usuarios, Habitos, Seguimientos, Logros
from .serializers import UsuarioSerialzer, HabitosSerializer, SeguimientoSerializer, LogrosSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    # conjunto de datos query que consulta todo de la tabla usuariarios
    queryset = Usuarios.objects.all()
    # permisos para hacer las consultas
    permission_classes = [permissions.AllowAny]
    # serializers  para convertir los datos de python a json
    serializer_class = UsuarioSerialzer

class HabitosViewset(viewsets.ModelViewSet):
    queryset = Habitos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HabitosSerializer

class SeguimientoViewset(viewsets.ModelViewSet):
    queryset = Seguimientos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeguimientoSerializer

class LogrosViewset(viewsets.ModelViewSet):
    queryset = Logros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LogrosSerializer