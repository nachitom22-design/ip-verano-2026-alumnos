# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

def home(request):

    """
    Muestra la pagina principal con todas las imagenes de los personajes.

    1- Obtiene todas las imagenes desde el services.getAllImages().
    2- Crea una lista vacia para los favoritos (en este punto no se muestran los favoritos).
    3- Renderiza el template 'home.html' enviando las imagenes y favoritos.
    """
    images= services.getAllImages() # Trae todas las imagenes desde el services 

    favourite_list= [] # Lista vacia de favoritos 

    return render(request, 'home.html', {'images': images,'favourite_list': favourite_list})

def search(request):

    """
    Busca personajes por nombre.

    1- Verifica que la solicitud sea POST.
    2- Obtiene el texto ingresado en el campo 'query'.
    3- Si el campo está vacío, redirige al home.
    4- Filtra las imagenes por nombre usando services.filterByCharacter(query).
    5- Renderiza el home con los resultados filtrados
    """
    if request.method == "POST":
        query = request.POST.get('query', '').strip() # Texto buscado

        
        if not query:
            return redirect('home') # Si el campo está vacío, redirige al home

        
        images = services.filterByCharacter(query) # Filtra por nombre

       
        favourite_list = [] # Lista vacia de favoritos

        return render(request, 'home.html', {
            'images': images,
            'favourite_list': favourite_list
        })

    
    return redirect('home')

    pass

def filter_by_status(request):

    """
    Filtra personajes por su estado (Alive o Deceased).

    1- Verifica que la peticion sea POST.
    2- Obtiene el estado desde el formulario.
    3- Si no hay estado, redirige al home.
    4- Filtra las imagenes por estado usando services.filterByStatus(status).
    5- Si el usuario esta logueado, obtiene su lista de favoritos, sino deja la lista vacia.
    6- Renderiza el home con los resultados.
    """

    if request.method == "POST":
        status = request.POST.get('status', '').strip()  # Alive o Deceased
        
        if not status:
            return redirect('home')

        images = services.filterByStatus(status) # Filtra por estado

        # Obtiene favoritos si el usuario esta autenticado, sino lista vacia
        if request.user.is_authenticated:
            favourite_list = services.getAllFavourites(request)
        else:
            favourite_list = []

        return render(request, 'home.html', {
            'images': images,
            'favourite_list': favourite_list
        })

    return redirect('home')

    pass

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    """
    pass

@login_required
def saveFavourite(request):
    """
    Guarda un personaje como favorito.
    """
    pass

@login_required
def deleteFavourite(request):
    """
    Elimina un favorito del usuario.
    """
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')