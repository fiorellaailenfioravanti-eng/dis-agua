from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
#Decoradores para permisos (opcional)

#para añadir permisos desde el backend
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404 # Agrega get_object_or_404 aquí
#validar grupos a los que pertenece el usuario
#esto seria lo mismo que el filtro en el frontend que se implemento en distribuidora/grupos.py
def es_vendedor_o_admin(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()
#CRUD
#Aca empeiza Read

def listar_productos(request):
    listar_productos = Producto.objects.all()
    #esto es para filtrar por categoria
    parametro_categoria = request.GET.get('categoria',"").strip()
    if parametro_categoria:
        listar_productos = listar_productos.filter(categoria__nombre__icontains=parametro_categoria)

    #obtener todos los productos mediante contexto
    contexto = {
        'productos': listar_productos,
        'categorias': Categoria.objects.all()
    }
    return render(request, 'listar_productos.html', contexto)
# Create your views here.



def ver_producto(request, pk):
    try:
        #obtener detalles de un producto específico mediante contexto
        producto = Producto.objects.get(id_producto=pk)
        contexto = {
            'producto': producto
        }
        return render(request, 'ver_producto.html', contexto)
    
    except Producto.DoesNotExist:
        return render(request, 'ver_producto.html', {'producto': None})

#Aca termina Read   
    


#Create
#MI DECORADOR SERIA ESTE PARA QUE VERIFIQUE SI ES VENDEDOR
@user_passes_test(es_vendedor_o_admin)
#este seria para comprar o añadir a lista de deseos
#abajo le estoy diciendo que debe ser administrador o vendedor para crear productos
# @permission_required('apps.productos.add_producto', raise_exception=True) #lo ultimo devuelve al usuario a login en caso de error
def crear_producto(request):   
    
    
    if request.method == 'POST':
        #post recibe información del formulario
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos')

    else:
        #get 
        form = ProductoForm()   
        return render(request, 'crear_producto.html', {'form': form})
    
@user_passes_test(es_vendedor_o_admin)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

#Update
@user_passes_test(es_vendedor_o_admin)
def editar_producto(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos')
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'form': form, 'producto': producto})





#Delete 
@user_passes_test(es_vendedor_o_admin)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('apps.productos:listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})