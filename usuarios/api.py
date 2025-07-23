from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import  UserSerializer
from django.contrib.auth.models import User
from .models import Usuarios
from rest_framework.authtoken.models import Token
from rest_framework import status 
from django.shortcuts import get_object_or_404

from usuarios.models import Usuarios, Habitos, Seguimientos, Logros
from .serializers import UsuarioSerialzer, HabitosSerializer, SeguimientoSerializer, LogrosSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token":token.key, "user":serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        # crear un modelo guardarlo en la base
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response("You are login with {}".format(request.user.username), status=status.HTTP_200_OK)

# from rest_framework.permissions import IsAuthenticated
# libreria para restringir rutas y enviar al login 
from django.utils.decorators import method_decorator

class UsuarioViewset(viewsets.ModelViewSet):
    # permisos para hacer las consultas de JWT pero lo puedo poner en el settings.py por defecto e todas las rutas    
    permission_classes = [permissions.AllowAny]
    # conjunto de datos query que consulta todo de la tabla usuariarios
    queryset = Usuarios.objects.all()
    # serializers  para convertir los datos de python a json
    serializer_class = UsuarioSerialzer


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class HabitosViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = Habitos.objects.all()
    serializer_class = HabitosSerializer

class SeguimientoViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = Seguimientos.objects.all()
    serializer_class = SeguimientoSerializer

class LogrosViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = Logros.objects.all()
    serializer_class = LogrosSerializer