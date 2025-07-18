import cv2
from cv2 import *
import face_recognition as fr
#import dlib
#import cmake

# Cargar imagenes

foto_control = fr.load_image_file('img4.jpg')
foto_prueba = fr.load_image_file('img5.jpg')

# Procesamiento de colores. pasar imagenes a RGB

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control

lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0] # indice 0

# Localizar cara control

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0] # indice 0

# Dibujar rectángulo

cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2)

# Realizar comparacion

resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B, tolerance=0.6)
print(resultado)  # >> TRUE

# Medida de la distancia

distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
print(distancia)

# Mostrar resultado

cv2.putText(foto_prueba,
            f'{resultado}{distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2)

# Mostrar imagenes

cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# Mantener programa abierto
cv2.waitKey(0)