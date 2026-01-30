from django.urls import path
from .views import registrar_usuario, ingresar_usuario, cerrar_sesion

app_name = 'apps.autenticacion'

urlpatterns = [    # Aquí puedes agregar las rutas de autenticación
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]
 