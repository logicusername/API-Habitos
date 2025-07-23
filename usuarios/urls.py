from rest_framework import routers
from .api import UsuarioViewset, HabitosViewset, SeguimientoViewset, LogrosViewset

router = routers.DefaultRouter()

# modelo de donde vienen las rutas
router.register('api/usuarios', UsuarioViewset, 'usuarios')
router.register('api/habitos', HabitosViewset, 'habitos')
router.register('api/seguimiento', SeguimientoViewset, 'seguimiento')
router.register('api/logros', LogrosViewset, 'logros')
urlpatterns = router.urls