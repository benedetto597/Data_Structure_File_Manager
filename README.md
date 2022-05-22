<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/CEUTEC_HONDURAS.png/1200px-CEUTEC_HONDURAS.png" style="width:250px"> </img>

<!-- Encabezado -->
### Estructura de datos II
#### Mayo 2022
#### Autor 

| Nombre | Correo |
|:-------:|:-----:|
| NOMBRE | [Ceutec](mailto:example@email.com) |

</div>

_____
_____
### Desarrollo del Proyecto
* Crear un programa en el lenguaje de programación de su preferencia que pueda realizar las siguientes operaciones:
    1. Leer registros de un archivo de datos.
    2. Escribir registros en un archivo de datos.
    3. Eliminar registros de un archivo de datos.
    4. Manejar la lista de disponibles.
    5. Compactar espacio no utilizado en el archivo de datos.
    6. Manejar un índice primario.

* Consideraciones
  * El archivo de datos en cuestión será un archivo plano, de texto (.TXT) llamado Proyecto1.txt
  * Cada registro será representado mediante una fila
  * Todas las filas tendrán una cantidad fija de caracteres
  * Algunos tipos de campos que pueden utilizarse son: 
    * campo numérico (a)
    * campo alfanumérico (b) 
    * campo numérico con decimales (c)
    * campo fecha (d)
  * Usar Tabulate para imprimir de forma matricial los datos

1. Leer
  * Debe ser posible navegar a través de los diferentes campos / registros.
  * El programa debe permitir que se lea y se vea el detalle de un registro específico seleccionado por el usuario. Es decir ver solamente el detalle de un registro que se busque basado en algún campo. Esta consulta debe realizarse a través del índice.
  * Al hacer la primera lectura del archivo deberá determinar cuántos registros hay, cuántos han sido eliminados (si hay eliminados), y con cuánto espacio se cuenta para ingresar nuevos registros (ver lista de disponibles).

2. Escribir
  * Los datos numéricos y de fecha deberán ingresarse en un formato reconocido por el usuario, pero deberán adecuarse al formato del archivo antes de ser grabados.
  * Antes de grabar un registro deberá determinar (basándose en la lista de disponibles) si es posible guardar el registro en un espacio dejado por algún registro. Si no encuentra ningún espacio deberá grabar el registro al final del archivo, si lo encuentra deberá grabarlo y registrar los datos utilizando el formato correcto de cada registro.
  * Al momento de grabar un registro además de los campos, debe grabarse el número de registro (campo longitud al inicio del registro) y también modificar la lista de disponibles si se viera afectada
  * Una vez que el registro se almacene debe actualizarse la lista de disponibles y el archivo de índices.

3. Eliminar 
  * Eliminar por posision
  * Al eliminar un registro deberá crear un nuevo registro en la lista de disponibles e indicando la cantidad de bytes disponibles.
  * Al eliminar un registro deberá eliminar el registro correspondiente del archivo de índices.
  * El espacio en el registro deberá ser sustituido por algún carácter que permita identificar que todo el registro se encuentra borrado. 

_____

### Documento del proyecto 
    1. Planteamiento del problema 
       1. Definición del problema
          1. Lectura y escritura de datos controlada con estructuras de datos conocidas en archivos de texto plano.
       2. Resolucion del problema 
          1. Abstraer el concepto de lista enlazada tipo cola con la opcion de añadir en una posicion especifica
          2. Abstraer lo obtenido de los archivos como el objeto **Contenido** y el contenido puede ser normalizado en una lista de **Registros**
          3. Crear funciones de lectura y escritura de archivos como clases independientes
          4. Gestionar el contenido del archivo mediante listas enlazadas, para separar los registros totales, de lo disponible y lo eliminado
          5. Construir el archivo de indices para gestionar la ultima version del archivo de registros
    2. Descripción del archivo de datos
       1. main.py --> archivo principal del programa
       2. src --> Carpeta con las funciones necesarias para resolver el problema planteado
       3. data --> Carpeta con los archivos de texto plano necesarios para resolver el problema
    3. Lenguaje de programación y requerimientos para ejecución 
       1. Lenguaje de programación: Python
       2. Requerimientos para la ejecución: 
          1. Python > 3.6
            * [Descargar Python](https://www.python.org/downloads/release/python-3104/)
          2. Pip (gestor de paquetes de python)
            * [Descargar pip.py](https://bootstrap.pypa.io/get-pip.py)
            * Luego ejecutar en una terminal el siguiente comandos (en la ubicacion del archivo)
              ```py
              python get-pip.py
              ```
          3. Tabulate (Print tables)
            * Ejecutar el siguiente comando en una terminal:
              ```py
              pip install tabulate
              ```
          4. Regex (Regular expressions)
            * Ejecutar el siguiente comando en una terminal:
              ```py
              pip install regex
              ```
           
    4. Breve descripción del código 
    5. Bitácora del proyecto
    6. Guía de instalación
       1. Instalar python
       2. Instalar pip 
       3. Instalar tabulate
       4. Instalar regex
    7. Comandos de ejecución
      1. Abrir una terminal en la ubicacion de **main.py** y ejecutar el comando:
        ```py
        python main.py
        ```
      2. Seleccionar una de las opciones desplegadas por el menu de opciones
      
    8.  Vídeo en youtube

_____

### Faltantes 
Leer --> Al hacer la primera lectura del archivo deberá determinar cuántos registros hay, cuántos han sido eliminados (si hay eliminados), y con cuánto
espacio se cuenta para ingresar nuevos registros (ver lista de disponibles).

Escribir 
--> Antes de grabar un registro deberá determinar (basándose en la lista de
disponibles) si es posible guardar el registro en un espacio dejado por algún
registro. Si no encuentra ningún espacio deberá grabar el registro al final
del archivo, si lo encuentra deberá grabarlo y registrar los datos utilizando
el formato correcto de cada registro.
--> Una vez que el registro se almacene debe actualizarse la lista de
disponibles y el archivo de índices.