"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*100) 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Indicar el tipo de ordenamiento")
    print("3- Consultar los videos con mas views y  son tendencia")
    print("4- Videos por categoria")
    print("0- Salir")

def initdicci(lista:str):
    """
    Inicializa el catalogo de libros
    """
    return controller.initdicci(lista)

def loadData(dicci):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(dicci)

def loadOrdenamientos(tipo,dicci,size):

    return controller.loadOrdenamientos(tipo,dicci,size)

def loadpaises(dicci,ppais,categgoria,cantidad):

    return controller.loadppaises(dicci,ppais,categgoria,cantidad)


dicci = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        x = str(input("Indique el tipo de lista que quiere: "))
        dicci = initdicci(x)
        loadData(dicci)
        primer= lt.firstElement(dicci["videos"])
        lista=[]
        categor= dicci["categorias"]["elements"]
        print('Videos cargados: ' + str(lt.size(dicci['videos'])))
        print('Categorias cargadas: ' + str(lt.size(dicci['categorias'])))
        print("el primer video: "+" Titulo : "+str(primer["title"])+" , "+" Nombre del canal:  "+str(primer["channel_title"])+" , "+" Fecha de tendencia: "+str(primer["trending_date"])+" , " +" Pais: "+str(primer["country"])+" , "  + " Vistas: "+str(primer["views"])+" , "+"  Me gustas: "+str(primer["likes"])+", "+ "Nomegustas :"+str(primer["dislikes"]))
        for i in categor:
             for t  in i:
                 hol=str(i[t])
                 lista.append((hol[0:2],hol[4:]))
        print(" Lista de categorias : "+ str(lista))   



   
    elif int(inputs[0]) == 2:   
        
        ordenamiento = str(input("Indique el tipo de ordenamiento que quiere utilizar(merge,quick,shell,selection,insertion): "))
        size = int(input("Indique el tamaño de la muestra: "))
        resultado = controller.loadOrdenamientos(str(ordenamiento),dicci,size)    
        print("Para el ordenamiento" + str(ordenamiento)+ ", el tiempo (mseg) es: "+ str(resultado[1]))

    elif int(inputs[0]) == 3: 

        ppais=str(input("Ingrese el nombre del pais deseado: "))
        categgoria=str(input("Ingrese el nombre de la categoria deseada :"))
        cantidad=int(input("Ingrese la cantidad deseada de videos: "))

        rt=loadpaises(dicci,ppais,categgoria,cantidad)

        print(rt)



    else:
        sys.exit(0)

sys.exit(0)

