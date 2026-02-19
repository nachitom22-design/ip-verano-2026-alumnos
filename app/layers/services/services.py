# capa de servicio/lógica de negocio

import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages():

    """
    Obtiene todas las imagenes de personajes desde la API y las convierte en objetos card.

    1- Llama a transport.getAllImages() para obtener los datos crudos de la API.
    2- Recorre cada personaje recibido.
    3- Convierte cada personaje en un objeto card usando translator.fromRequestIntoCard().
    4. Guarda cada card en una lista.
    5- Retorna la lista final de Cards.
    """

    data = transport.getAllImages() # Trae los datos desde la API

    cards = [] # Lista donde se guardaran las cards convertidas

    for character in data:
        # Convierte el personaje en un objeto Card
        card = translator.fromRequestIntoCard(character)
        cards.append(card) # Agrega la card a la lista

    return cards # Retorna todas las cards  

def filterByCharacter(name):
    """
    Filtra las cards de los personajes segun el nombre proporcionado.

    1- Obtiene todas las cards disponibles.
    2- Recorre cada card.
    3- Compara si el nombre buscado esta contenido dentro del nombre del personaje (ignorando mayúsculas).
    4- Devuelve solo las cards que coinciden.
    """
    all_cards = getAllImages() # Obtiene todas las cards

    # Filtra las cards cuyo nombre contiene el texto buscado (ignorando mayúsculas)
    filtered = [card for card in all_cards if name.lower() in card.name.lower()]
    
    return filtered # Retorna la lista filtrada


    pass

def filterByStatus(status_name):

    """
    Filtra las cards de los personajes segun su estado (Alive o Deceased).
    
    1- Obtiene todas las cards.
    2- Recorre cada card.
    3- Compara el estado de la card con el estado recibido (ignorando mayúsculas).
    4- Devuelve solo las cards que coinciden con el estado buscado.
    """

    all_cards = getAllImages() # Obtiene todas las cards

    # Filtra por estado, comparando el estado de cada card con el estado buscado (ignorando mayúsculas)
    filtered = [card for card in all_cards if card.status.lower() == status_name.lower()]
    
    return filtered # Retorna la lista filtrada

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    """
    Guarda un favorito en la base de datos.
    
    Se deben convertir los datos del request en una Card usando el translator,
    asignarle el usuario actual, y guardarla en el repositorio.
    """
    pass

def getAllFavourites(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    
    Si el usuario está autenticado, se deben obtener sus favoritos desde el repositorio,
    transformarlos en Cards usando translator y retornar la lista. Si no está autenticado, se retorna una lista vacía.
    """
    pass

def deleteFavourite(request):
    """
    Elimina un favorito de la base de datos.
    
    Se debe obtener el ID del favorito desde el POST y eliminarlo desde el repositorio.
    """
    pass