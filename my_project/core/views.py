from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
