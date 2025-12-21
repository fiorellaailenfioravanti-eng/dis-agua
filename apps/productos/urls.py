from django.urls import path
from .views import listar_productos

urlpatterns = [
    # Aquí puedes agregar las rutas específicas de la aplicación 'productos'
    # CRUD
    # C = Crear producto 
    #path('crear', crear_producto, name='crear_producto'),

    # R = Leer productos
    path('', listar_productos, name='listar_productos'),
    #path('<int:id>', ver_producto, name='ver_producto'),

    # U = Actualizar producto
    #path('editar/<int:id>', editar_producto, name='editar_producto'),

    # D = Eliminar producto
    #path('eliminar/<int:id>', eliminar_producto, name='eliminar_producto'),
]