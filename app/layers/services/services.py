# capa de servicio/lógica de negocio

import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages():

    """
    Obtiene todas las imágenes de personajes desde la API y las convierte en objetos Card.
    
    Esta función debe obtener los datos desde transport, transformarlos en Cards usando 
    translator y retornar una lista de objetos Card.
    """
    data = transport.getAllImages()

    cards = []
    for character in data:
        card = translator.fromRequestIntoCard(character)
        cards.append(card)
    return cards

def filterByCharacter(name):
    all_cards = getAllImages()
    filtered = [card for card in all_cards if name.lower() in card.name.lower()]
    return filtered
    """
    Filtra las cards de personajes según el nombre proporcionado.
    
    Se debe filtrar los personajes cuyo nombre contenga el parámetro recibido. Retorna una lista de Cards filtradas.
    """

    pass

def filterByStatus(status_name):
    all_cards = getAllImages()
    filtered = [card for card in all_cards if card.status.lower() == status_name.lower()]
    return filtered

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