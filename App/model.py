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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newdicc(lista: str):
    """
    Inicializa el catálogo de los videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias ,
    Retorna el catalogo inicializado.
    """
    dicci = {'videos': None,
               'categorias': None,
              }
    if lista == "SINGLE_LINKED" or lista == "ARRAY_LIST":
        dicci['videos'] = lt.newList(lista,cmpfunction=cmpVideosByViews)
        dicci['categorias'] = lt.newList(lista)
    else:
        print("Esta tipo de lista no existe")


    return dicci


# Funciones para agregar informacion al catalogo
def addVideo(dicci, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(dicci['videos'], video)



def addCategoria(dicci, categoria):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(dicci['categorias'], categoria)




# Funciones para creacion de datos


    
        

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
   

def cmpVideosByViews(video1, video2):

    return (float(video1['views']) > float(video2['views']))

# Funciones de ordenamiento


def Ordenamientos(tipo,dicci,size):

    start_time = time.process_time()
    sub_list= lt.subList(dicci["videos"],0,size)
    sub_list = sub_list.copy()

    if tipo == "shell":
        x = sa.sort(sub_list,cmpVideosByViews)
    elif tipo == "selection":
        x = sel.sort(sub_list,cmpVideosByViews)
    elif tipo == "insertion":
        x = ins.sort(sub_list,cmpVideosByViews)
    else:
        print("Este tipo de ordenamiento no existe")
    
  
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return x, elapsed_time_mseg

   
  

