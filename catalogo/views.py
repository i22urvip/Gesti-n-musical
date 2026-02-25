from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Obra, Compositor
from .forms import ObraForm, RegistroForm, CompositorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def lista_obras(request):
    # Capturamos todos los parámetros de la URL
    query = request.GET.get('q')
    compositor_id = request.GET.get('compositor')
    tipo = request.GET.get('tipo')
    orden = request.GET.get('orden') # ¡NUEVO! Capturamos cómo quiere ordenar el usuario
    
    # Empezamos con TODAS las obras (quitamos el order_by de aquí para hacerlo dinámico luego)
    obras = Obra.objects.all()
    compositores = Compositor.objects.all()

    # 1. Filtramos (el embudo)
    if query:
        obras = obras.filter(titulo__icontains=query)
    if compositor_id:
        obras = obras.filter(compositor_id=compositor_id)
    if tipo:
        obras = obras.filter(tipo=tipo)

    # 2. Ordenamos según lo que haya elegido el usuario
    if orden == 'duracion':
        obras = obras.order_by('-duracion_minutos') # El signo '-' significa de mayor a menor
    elif orden == 'antiguedad':
        obras = obras.order_by('ano_composicion')   # Sin signo '-' significa de la más antigua a la más moderna
    else:
        # Por defecto, si no elige nada o elige 'popularidad', mostramos las más visitadas primero
        obras = obras.order_by('-popularidad')

    contexto = {
        'obras': obras,
        'compositores': compositores,
        'tipos_obra': Obra.TIPOS_DE_OBRA,
        'query': query,
        'compositor_seleccionado': compositor_id,
        'tipo_seleccionado': tipo,
        'orden_seleccionado': orden, # ¡NUEVO! Se lo pasamos al HTML
    }
    
    return render(request, 'catalogo/lista_obras.html', contexto)

def detalle_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    # ¡NUEVO! Sumamos 1 a la popularidad y guardamos en la base de datos
    obra.popularidad += 1
    obra.save()
    return render(request, 'catalogo/detalle_obra.html', {'obra': obra})

# Obligamos a estar logueado para crear obras
@login_required 
def nueva_obra(request):
    if request.method == 'POST':
        # Capturamos los datos de texto y los archivos (request.FILES para el PDF)
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save(commit=False) # Pausamos el guardado
            obra.creador = request.user    # Le asignamos el usuario actual como creador
            obra.save()                    # Ahora sí, guardamos en base de datos
            return redirect('lista_obras') # Lo devolvemos a la lista principal
    else:
        form = ObraForm()
    
    return render(request, 'catalogo/obra_form.html', {'form': form})

@login_required
def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    
    # EL PORTERO: Comprobamos si el usuario actual NO es el creador y TAMPOCO es el superusuario (admin)
    if request.user != obra.creador and not request.user.is_superuser:
        raise PermissionDenied("¡Alto ahí! No tienes permiso para editar esta obra.")
        
    if request.method == 'POST':
        # Al pasarle 'instance=obra', Django sabe que no debe crear una nueva, sino actualizar la existente
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        # Rellenamos el formulario con los datos actuales de la obra
        form = ObraForm(instance=obra)
        
    return render(request, 'catalogo/obra_form.html', {'form': form, 'obra': obra})

def lista_compositores(request):
    compositores = Compositor.objects.all().order_by('nombre')
    return render(request, 'catalogo/lista_compositores.html', {'compositores': compositores})

def detalle_compositor(request, compositor_id):
    compositor = get_object_or_404(Compositor, id=compositor_id)
    # Gracias al related_name='obras' que pusimos en el models.py, 
    # podemos sacar todas las obras de este compositor fácilmente en el HTML
    return render(request, 'catalogo/detalle_compositor.html', {'compositor': compositor})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('lista_obras')
    else:
        form = RegistroForm()
    return render(request, 'catalogo/registro.html', {'form': form})

# Vista para Crear Compositor
@login_required
def nuevo_compositor(request):
    if request.method == 'POST':
        form = CompositorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo/lista_compositores')
    else:
        form = CompositorForm()
    return render(request, 'catalogo/nuevo_compositor.html', {'form': form})

# Vista para Eliminar Compositor (Solo Administradores)
@login_required
def eliminar_compositor(request, compositor_id):
    if not request.user.is_superuser:
        return redirect('lista_compositores')

    compositor = get_object_or_404(Compositor, id=compositor_id)

    if request.method == 'POST':
        compositor.delete()
        return redirect('lista_compositores')

    return render(request, 'catalogo/eliminar_compositor.html', {'compositor': compositor})