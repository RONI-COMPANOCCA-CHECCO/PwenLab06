from django.shortcuts import render, redirect
from mi_proyecto.tienda.models import Venta
from .forms import VentaForm

# Create your views here.
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
        else:
            form = VentaForm()
        return render(request, 'tienda/crear_venta.html', {'form': form})
    
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'tienda/lista_ventas.html', {'ventas': ventas})