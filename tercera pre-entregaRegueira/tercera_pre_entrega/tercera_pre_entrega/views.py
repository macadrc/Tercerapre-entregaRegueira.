from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, BusquedaForm
from .models import Producto

def index(request):
    return render(request, 'index.html')

def insertar_datos(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if producto_form.is_valid() and cliente_form.is_valid():
            producto_form.save()
            cliente_form.save()
            return redirect('index')  
    else:
        producto_form = ProductoForm()
        cliente_form = ClienteForm()
    return render(request, 'insertar_datos.html', {'producto_form': producto_form, 'cliente_form': cliente_form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data.get('termino_busqueda')
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})
