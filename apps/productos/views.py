from django.shortcuts import render

def listar_productos(request):
    return render(request, 'listar_productos.html')
# Create your views here.
