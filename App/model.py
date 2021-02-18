"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de los videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias ,
    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categorias': None,
              }

    catalog['videos'] = lt.newList()
    catalog['categorias'] = lt.newList('SINGLE-LINKED')

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    categorias = video['categorias'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for cat in categorias:
        addCategoria(catalog, cat.strip(), video)

def addCategoria(catalog, categoria, video):
    """
    Adiciona un categoria a lista de videos, la cual guarda referencias
    a las categorias de dicha canción
    """
    categorias = catalog['categorias']
    poscat = lt.isPresent(categorias, categoria)
    if poscat > 0:
        categoria = lt.getElement(categorias, poscat)
    else:
        categoria = newCategoria(categoria)
        lt.addLast(categorias, categoria)
    lt.addLast(categoria['videos'],video)

# Funciones para creacion de datos

def newCategoria(name):
    """
    Crea una nueva estructura para modelar los videos de
    una categoria
    """
    categoria = {'name': "", "videos": None}
    categoria['name'] = name
    categoria['videos'] = lt.newList('ARRAY_LIST')
    return categoria

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento