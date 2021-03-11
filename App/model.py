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
from operator import itemgetter
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qk
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
                    "pais":None,
                    }
    if lista == "LINKED_LIST" or lista == "ARRAY_LIST":
        dicci['videos'] = lt.newList(lista,cmpfunction=cmpVideosByViews)
        dicci['categorias'] = lt.newList(lista)
        dicci["pais"]={}
        
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

def cmpPaisesbyviews(ll1,ll2):

    return(float(ll1["views"])>float(ll2["views"]))

def cmpCategoriesByTrending(cat1, cat2):

    return (float(cat1['title']) > float(cat2['title']))

def cmpPaisesbylikes(lili1,lili2):

    return(float(lili1["likes"])>float(lili2["likes"]))


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
    elif tipo == "quick":
        x = qk.sort(sub_list,cmpVideosByViews)
    elif tipo == "merge":
        x = mg.sort(sub_list,cmpVideosByViews)
    else:
        print("Este tipo de ordenamiento no existe")
    
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return x, elapsed_time_mseg

   
  
def paises(dicci):
    

    for m in range(0,lt.size(dicci["videos"])):
        rta=lt.getElement(dicci["videos"],m)
    
    
    
        if rta["country"] not in dicci["pais"]:
            dicci["pais"][rta["country"]]=lt.newList()
            lt.addLast(dicci["pais"][rta["country"]],rta)

        else:
            lt.addLast(dicci["pais"][rta["country"]],rta)

    

    
    return dicci


def requerimiento1(dicci,ppais:str,categorias:str,cantidad:int):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    ct=categori[categorias]
    ll=lt.newList()
    jlo=lt.newList()
    
    
    for m in range(0,lt.size(dicci["pais"][ppais])):
        rta=lt.getElement(dicci["pais"][ppais],m)


        if rta["category_id"]==str(ct):

            lt.addLast(ll,rta)
        
    x = mg.sort(ll,cmpPaisesbyviews)

    for i in range(cantidad):
        tt=lt.getElement(x,i)
        
        lt.addLast(jlo,(tt["trending_date"],tt["title"],tt["channel_title"],tt["publish_time"],tt["views"],tt["likes"],tt["dislikes"]))
    
  
    return jlo

    
def TrendingVideo(dicci,pais:str):

    diccionario = {}

    for i in range(1,lt.size(dicci["pais"][pais])): 
        video = lt.getElement(dicci["pais"][pais],i)

        if video["video_id"] in diccionario:
            diccionario[video["video_id"]]+=1

        else:
            diccionario[video["video_id"]]=1

    lista = []
    for i in diccionario:
        lista.append(diccionario[i])
        maxi = max(lista)

        tupla = (video["title"],video["channel_title"],video["country"],maxi)


    return tupla

        


def requerimiento3(dicci,categorii:str):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    ct=categori[categorii]
    pt= lt.newList()
    dt={}
    numero=0
    
    for i in range(0,lt.size(dicci["videos"])):
        rta=lt.getElement(dicci["videos"],i) 


        if rta["category_id"]==str(ct):

            lt.addLast(pt,rta)
        
    for p in range(0,lt.size(pt)):

        tt=lt.getElement(pt,p)

        if tt["title"]not in dt:

            dt[tt["title"]]=[1,(tt)]
        else:
            dt[tt["title"]][0]+=1



    for i in dt:
        if dt[i][0] > numero:
            numero= dt[i][0]
            tt=(("El titulo del video : "+str(dt[i][1]["title"])," El nombre del canal: "+str(dt[i][1]["channel_title"]),"el category id: "+str(dt[i][1]["category_id"]),"los dias que ha sido trending: "+str(dt[i][0])))
            
       

   
    return tt




def organizartags(dicci):
    pala=""
    lista=[]
    ll=[]


    for i in range(0,lt.size(dicci["videos"])):

        rta=lt.getElement(dicci["videos"],i) 

        for mm in rta["tags"]:

            if mm != "|"and  mm!='"':

                pala+=mm
            else:
                lista.append(pala)
                pala=""

        for pp in lista:

             if pp !='':

        
                 ll.append(pp)


        
        rta["tags"]=ll
        ll=[]

      
    return dicci


def requerimiento4(dicci,tag:str,numero:int):
    lili=lt.newList()
    lastima=[]

    for i in range(0,lt.size(dicci["videos"])):

        rta=lt.getElement(dicci["videos"],i) 

        if tag in rta["tags"]:

            lt.addLast(lili,rta)

    x = mg.sort(lili,cmpPaisesbylikes)

    for i in range(numero):
        tt=lt.getElement(x,i)

        lastima.append(("titulo: "+str(tt["title"])," Nombre del canal: "+str(tt["channel_title"])," Fecha de publicacion: "+str(tt["publish_time"])," Visitas: "+str(tt["views"])," Me gustas"+str(tt["likes"]),"No me gustas: "+str(tt["dislikes"])))



    return lastima
        
        
    































