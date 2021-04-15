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
 """
import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initdicci(lista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    dicci = model.newdicc(lista)
    return dicci

# Funciones para la carga de datos

def loadData(dicci):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(dicci)
    loadCategorias(dicci)

def loadVideos(dicci):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videofile = cf.data_dir + 'videos-20pct.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(dicci, video)


def loadCategorias(dicci):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    Categoryfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(Categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addCategoria(dicci, category)
   
   
# Funciones de ordenamiento

def loadOrdenamientos(tipo,dicci,size):
    rta = model.Ordenamientos(tipo,dicci,size)
    return rta

# Funciones de consulta sobre el catálogo

def loadppaises(dicci):

    rttaa = model.paises(dicci)

    return rttaa



def loadrequerimineto1(dicci,ppais,categorias,cantidad):

    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    jes=model.requerimiento1(dicci,ppais,categorias,cantidad)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return jes,delta_time, delta_memory 

def loadTrendingVideo(dicci,pais):

    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    ta=model.TrendingVideo(dicci,pais)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return ta,delta_time, delta_memory


def loadrequerimiento3(dicci,categorii):

    
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    uu=model.requerimiento3(dicci,categorii)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return uu,delta_time, delta_memory
def loadorganizartags(dicci):

    opo=model.organizartags(dicci)

    return opo

def loadrequerimiento4(dicci,tag,numero):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()


    pomona=model.requerimiento4(dicci,tag,numero)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return pomona,delta_time, delta_memory


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory