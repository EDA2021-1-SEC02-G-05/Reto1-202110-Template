1) ¿Cuáles son los mecanismos de interacción (I/O: Input/Output) que tiene el view.py con el usuario?

En el view los mecanismos de interacción respecto al input es básicamente pedirle al usuario en primer lugar 
la información de los archivos en general. La opción 2 le pide los libros top por promedio. La tercera opción 
le pide los libros de un autor en específico, teniendo en cuenta que si no aparece el autor aparecerá que el autor
 ingresado no existe. Por último, dividir los libros por género. En cuanto a los outputs, se puede apreciar en primer 
 lugar que al pedir la información en general se va a suministrar la información de la cantidad de libros, autores y géneros.
 Si queremos el top de libros, va a suministrar los primeros libros que indique el usuario.

2) ¿Cómo se almacenan los datos de GoodReads en el model.py?

Una vez creadas las listas vacias, se llama la lista vacia y en corchetes cuadrados se pone el nombre 
del archivo Goodreads y se le asigna un lt.newlist. Para agregra información a la lista vacia, en la 
primera función llamada addbook, con lt.addlast luego llamando la lista vancia catalog y dentro de los 
corchetes cuadrados el nombre del archivo goodreads que se quiere añadir

3) ¿Cuáles son las funciones que comunican el view.py y el model.py?

Las funciones que comunican el view con el model son las que en el model crean las funciones de consulta. 
Por ejemplo, getBooksByAuthor, getBestBooks,countBooksByTag. En el view la funcion crea una variable donde llama 
al controlador y llama posteriormentre la funcion que quiere del model con sus respectiuvos parametros

4) ¿Cómo se crea una lista?

Se crea una funcion con los parametro que se deseen, y asi se crea una lista vacía. 
Luego se crea una variable que se le asigna el lt.newlist y dentro como parámetros va los nombres que se crearon antes

5) ¿Qué hace el parámetro cmpfunction=None en la función newList()?

El cmpfunction=None compara los elementos de una lista

6) ¿Qué hace la función addLast()?

addLast un elemento en la ultima posición de la lista

7) ¿Qué hace la función getElement()?

getElement retorna el elemento en la posición pos de la lista. pos es el que entra por parámetro indicado

8) ¿Qué hace la función subList()?

La función sublist brinda una nueva lista que contiene los elementos de una parte de una lista según la posicion que indique el usuario

9) ¿Observó algún cambio en el comportamiento del programa al cambiar la implementación del parámetro “ARRAY_LIST” a “SINGLE_LINKED”?

El tiempo de ejecuciòn de la carga de los datos fue mucho mayor en el Single Linked que en el Array list