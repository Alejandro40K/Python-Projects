# Compararemos una lista de fotos con una imagen tomada por la camara

import cv2
import numpy
from cv2 import *
import face_recognition as fr
import os
from datetime import datetime

# Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)


for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

# Codificar imagenes
def codificar(imagenes):
    # crear una lista nueva
    lista_codificada = []
    # pasa imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)[0]
        # agregar a la lista
        lista_codificada.append(codificado)
    # devolver la lista codificada
    return lista_codificada


def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])
    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


# lista conto todas las fotos codificadas y en RGB
lista_empleados_codificada = codificar(mis_imagenes)

# Tomar una imagen con camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la camara
exito, imagen = captura.read()
if not exito:
    print('No se ha podido tomar la captura')
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    # codificar a cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    # Buscar coincidencias entre captura y lista fotos
    for cara_codif, cara_ubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, cara_codif)
        distancias = fr.face_distance(lista_empleados_codificada, cara_codif)
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con ninguno de nuestros empleados')
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            # Mantener ventana abierta
            # Almacenar los cuatro puntos de cada rectangulo
            y1,x2,y2,x1 = cara_ubic

            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

            registrar_ingresos(nombre)
            # mostrar la imagen obtenida
            cv2.imshow('Imagen Web', imagen)
            # Mantener ventana
            cv2.waitKey(0)


# Leer imagen
print(len(lista_empleados_codificada))
print(nombres_empleados) # sin terminacion jpg