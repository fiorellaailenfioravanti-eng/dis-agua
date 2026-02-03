from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from apps.productos.models import Producto
from django.urls import reverse
from django.contrib import messages


# Create your views here.
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not creado:
        item_carrito.cantidad += 1
        item_carrito.save()
    
    # LÓGICA INTELIGENTE: Si viene de 'ver_producto', vuelve ahí. 
    # Si no, vuelve al catálogo.
    referer = request.META.get('HTTP_REFERER')
    if referer and 'ver_producto' in referer: # Ajusta 'ver_producto' a como sale en tu URL de detalle
        return redirect('apps.productos:ver_producto', pk=producto.id_producto)
    messages.success(request, f"{producto.nombre} se añadió al carrito.")
    return redirect('apps.productos:listar_productos')

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    contexto = {
        'carrito': carrito,
        'items': carrito.items.all(),
        'total_precio': carrito.total_precio(),
    }
    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required
def eliminar_del_carrito(request, item_id):
    carrito= get_object_or_404(Carrito, usuario=request.user)
    item = carrito.items.filter(id=item_id).first()
    if item:
        item.delete()
    return redirect('apps.carrito:ver_carrito')

@login_required
def vaciar_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.items.all().delete()
    return redirect('apps.carrito:ver_carrito')

