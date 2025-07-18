"""
Proyecto: Recetario
Nombre: Alejandro Orozco Romo
Fecha: 27/06/2025

Metodos importados: import os =  proporciona funciones para interactuar con el sistema operativo
                    from pathlib import Path = puede interpretar cualquier ruta, path es un objeto
                    PureWindowsPath = tambien de pathlib, transforma cualquier tipo de ruta en una ruta de windows
                    from os import system = usamos system para limpiar la consola

Metodos utilizados:

                    os.getcwd() = nos proporciona la ruta actual de trabajo
                    os.chdir() = establece otra ruta de trabajo
                    os.makedirs() = nos permite crear directorios
                    os.path.basename(ruta) = nos permite obtener el nombre del archivo donde estamos
                    os.path.dirname(ruta) = nos permite obtener solo el directorio donde nos encontramos
                    os.path.split(ruta) = nos devuelve los elementos en una tupla
                    os.rmdir(ruta) = nos permite eliminar un directoio

                    Path(ruta) = no importa el formato de la ruta, cualquier usuario podra abrir los codigos
                    read_text() = nos permite leer el conrenido del archivo sin necesidad de abrir ni cerrar el archivo, ejem: carpeta.read_text()
                    name = nos permite conocer el nombre del archivo
                    suffix = nos da el sufijo del archivo, osea su terminacion, ejem: .txt
                    stem = nos da el nombre del archivo sin el tipo

                    isnumeric() = nos sirve para determinar su un caracter es un numero
                    iterdir() = este metodo nos sirve para iterar dentro del directorio
                    write_text() = metodo de Path, nos sirve para escribir en un texto
                    unlink() = metodo empleado para eliminar un archivo

Mejoras: Agregar un modo para cancelar antes al ingresar a una opcion
"""


## LIBRERIAS

from pathlib import Path
from os import system
import os

ruta = Path(Path.home(),'Recetas') # Usamos path home por que nos retorne el path absolto de home directory

## FUNCIONES

def contar_recetas(ruta):
    """
        Esta funcion busca en el con el metodo .glob() todos
        los archivos .txt almacenados en ruta.
    """
    contador = 0
    for archivo in Path(ruta).glob('**/*.txt'):
        contador +=1
    return contador

def menu_inicio():
    """
        Menu inicio, será la primera funcion en aparecer.
        No recibe ningun argumento, solo limpiara la pantalla
        y mostrara el menu de usuario
    """
    system('cls')
    print('*' * 50)
    print('*' * 5 +" Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en {ruta}')
    print(f'El total de recetas es {contar_recetas(ruta)}')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,7):
        print("Elige una opción")
        print( """
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa """)
        eleccion_menu = input()
    return int(eleccion_menu)

def elegir_categoria(lista):
    """
        Esta funcion nos permite elegir una categoria, para ello necesitamos
        una lista de las categorias
    """
    eleccion_correcta = 'x' # esta  variable nos asegura que entre al loop en la primera vuelta
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1): # como no conocemos cuantas categorias habra, el rango debe ser el largo de la lista de categorias +1
        eleccion_correcta = input("\nElije una categoria: ")
    return lista[int(eleccion_correcta) - 1]# nos regresa un elemento de la lista, (un indice) el cual ha sido elegido por el usuario

def mostrar_categoria(ruta):
    """
        Esta funcion muestra las categorias que tenemos en nuestro directorio
        primero se realiza una busqueda por medio de iterdir, el cual es un
        metodo que itera en nuestro directorio.
        Despues obtenemos mediante .name el nombre de la categoria, y almacenamos
        ese nombre en la lista interna que creamos, llamada lista categorias.
        Al final retornaremos esa lista.
    """
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name) # Obtenemos solo el nombre de la carpeta con name
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1 #contador se incrementa con cada pasada del loop
    return lista_categorias

def mostrar_recetas(ruta):
    """
        Esta funcion mostrará las recetas que existan en determinada categoria.
        para ello necesitamos crear una lista para guardar las recetas, para hacerlo
        usaremos un for para iterar en la ruta y buscar mediante .glob  todos los
        archivos *.txt, luego con name extraeremos solo sus nombres
        y los almacenaremos mediante append en la lista. Al final retornaremos
        la lista_recetas
    """
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}]-{receta_str}")
        lista_recetas.append(receta)
        contador+=1
    return lista_recetas

def elegir_recetas(lista):
    """
        funcion para elegir receta, toma una lista la cual emplea para mostrar las
        recetas disponibles
    """
    eleccion_receta = 'x' # siempre y cuando la eleccion no sea una letra, se inicia el loop
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista)+1):
        eleccion_receta = input("\nElije una receta")
    return lista[int(eleccion_receta)-1]


def leer_receta(receta):
    """
        Esta funcion leerá una receta del directorio, usando .read_text nos evitamos:
        abrir_receta = open(receta,'r')
        contenido = abrir_receta.read()
        abrir_receta.close()
    """
    print(Path.read_text(receta))



def crear_receta(ruta):
    """
        Función para crear una receta, para hacerlo necesitamos pasarle una
        ruta para saber hacia donde se creará dicha receta. Tenemos que pasar la
        ruta de la categoria elegida, y ademas debemos de comprobar si esa
        receta ya existe.
    """
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta) # creamos con path la ruta nueva, concatenamos la ruta donde estamos con el nuevo nombre de la receta
        if not os.path.exists(ruta_nueva): # si la ruta no existe
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")

def crear_categoria(ruta):
    """
        Función para crear una categoria, para hacerlo necesitamos pasarle una
        ruta para saber hacia donde se creará el directorio. Para crearlo usamos
        el metodo mkdir de Path para crear una nueva carpeta.,
    """
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria) # creamos con path la ruta nueva, concatenamos la ruta donde estamos con el nuevo nombre de la receta
        if not os.path.exists(ruta_nueva): # si la ruta no existe
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esa categoria ya existe")


def eliminar_receta(receta):
    """
        Esta funcion eliminara la receta con el metodo unlink de path, el
        cual eliminara el archivo
    """
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_directorio(categoria):
    """
        Función para eliminar la categoria, empleamos para ello el metodo mkdir para
        eliminar la categoria
    """
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    """
        Función para volver al inicio
    """
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu")

## CODIGO PRINCIPAL (Arbol de decicion)


finalizar_programa = False

while not finalizar_programa:
    menu = menu_inicio()

    if menu == 1:
        mis_categorias = mostrar_categoria(ruta) # es una lista de las categorias
        mi_categoria = elegir_categoria(mis_categorias) #ruta
        mis_recetas = mostrar_recetas(mi_categoria) #lista
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()


    elif menu == 3:
        crear_categoria(ruta)
        volver_inicio()


    elif menu == 4:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()


    elif menu == 5:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_directorio(mi_categoria)
        volver_inicio()


    elif menu == 6:
        finalizar_programa = True


    else:
        print("Opcion no valida")