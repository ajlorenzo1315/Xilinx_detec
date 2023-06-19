from tqdm import tqdm
import numpy as np
import cv2
import os

# Ruta del archivo de texto que contiene las direcciones de las imágenes
path_archivo = "./train_path.txt"

# Ruta de la carpeta donde se guardarán las imágenes redimensionadas
path_carpeta_destino = "./imagenes_redimensionadas/"

# Tamaño de la nueva imagen redimensionada
nuevo_tamano = (256, 256)

# Leemos el archivo de texto con las direcciones de las imágenes
with open(path_archivo, "r") as f:
    direcciones_imagenes = f.readlines()
    direcciones_imagenes = [direccion.strip() for direccion in direcciones_imagenes]

# Crear una barra de progreso dinámica para mostrar el progreso del procesamiento de imágenes
barra_progreso = tqdm(total=len(direcciones_imagenes), desc="Procesando imágenes")
# Recorremos cada dirección de imagen y redimensionamos las imágenes
for direccion_imagen in direcciones_imagenes:
    #print("CAMBIANDO TAMANO DE  {}",(direccion_imagen))
    imagen = cv2.imread(direccion_imagen)
    imagen_redimensionada = cv2.resize(imagen, nuevo_tamano)

    # Obtenemos el nombre de la imagen a partir de la dirección
    nombre_imagen = os.path.basename(direccion_imagen)

    # Guardamos la imagen redimensionada en la carpeta destino con el mismo nombre
    cv2.imwrite(os.path.join(path_carpeta_destino, nombre_imagen), imagen_redimensionada)

    # Actualizar la barra de progreso
    barra_progreso.update(1)

# Cerrar la barra de progreso
barra_progreso.close()
