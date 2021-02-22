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

def datosVideo(listaVideo:list)->dict:
     var = addVideo(catalog,video)
     while len(var) > 0:
        
        divdatos = var.split(",")
        
        datos = divdatos[0]
       
        if datos in videos:
            videos[datos].append([{"video_id":int(divdatos[1]),"trending_date":int(divdatos[2]),"title":int(divdatos[3]),"channel_title":float(divdatos[4]),"category_id":int(divdatos[5]),"publish_time":int(divdatos[6]),"tags":int(divdatos[7]),"views":float(divdatos[8],"likes":int(divdatos[9]),"dislikes":int(divdatos[10]),"comment_count":int(divdatos[11]),"thumbnail_link":float(divdatos[12],"comments_disabled":int(divdatos[13]),"ratings_disabled":float(divdatos[14]"video_error_or_removed":int(divdatos[15]),"description":int(divdatos[16]),"country":int(divdatos[17])}]
        else:
            videos[datos]=[{"video_id":int(divdatos[1]),"trending_date":int(divdatos[2]),"title":int(divdatos[3]),"channel_title":float(divdatos[4]),"category_id":int(divdatos[5]),"publish_time":int(divdatos[6]),"tags":int(divdatos[7]),"views":float(divdatos[8],"likes":int(divdatos[9]),"dislikes":int(divdatos[10]),"comment_count":int(divdatos[11]),"thumbnail_link":float(divdatos[12],"comments_disabled":int(divdatos[13]),"ratings_disabled":float(divdatos[14]"video_error_or_removed":int(divdatos[15]),"description":int(divdatos[16]),"country":int(divdatos[17])}]

    return videos

def addCategoria(catalog, categoria):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categorias'], categoria)



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento