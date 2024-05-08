import cv2
import os

def redimensionar_imagenes(carpeta_entrada, carpeta_salida):
    # Obtener la lista de carpetas en la carpeta de entrada
    carpetas = os.listdir(carpeta_entrada)
    
    # Iterar sobre cada carpeta en la carpeta de entrada
    for carpeta in carpetas:
        # Combinar la ruta completa de la subcarpeta de entrada
        ruta_subcarpeta_entrada = os.path.join(carpeta_entrada, carpeta)
        
        # Combinar la ruta completa de la subcarpeta de salida
        ruta_subcarpeta_salida = os.path.join(carpeta_salida, carpeta)
        
        # Crear la subcarpeta de salida si no existe
        if not os.path.exists(ruta_subcarpeta_salida):
            os.makedirs(ruta_subcarpeta_salida)
        
        # Obtener la lista de archivos en la subcarpeta de entrada
        archivos = os.listdir(ruta_subcarpeta_entrada)
        
        # Iterar sobre cada archivo en la subcarpeta de entrada
        for archivo in archivos:
            # Combinar la ruta completa del archivo de entrada
            ruta_entrada = os.path.join(ruta_subcarpeta_entrada, archivo)
            
            # Leer la imagen
            imagen = cv2.imread(ruta_entrada)
            
            if imagen is not None:
                # Redimensionar la imagen a 48x48 píxeles
                imagen_redimensionada = cv2.resize(imagen, (48, 48))
                
                # Combinar la ruta completa del archivo de salida
                ruta_salida = os.path.join(ruta_subcarpeta_salida, archivo)
                
                # Guardar la imagen redimensionada en la subcarpeta de salida
                cv2.imwrite(ruta_salida, imagen_redimensionada)
                
                print(f"Imagen redimensionada y guardada: {ruta_salida}")

# Rutas de las carpetas de entrada y salida
carpeta_train_entrada = "datasetGit/dataset/train"
carpeta_train_salida = "datasetGit/datasetRedimensionado/train"
carpeta_val_entrada = "datasetGit/dataset/val"
carpeta_val_salida = "datasetGit/datasetRedimensionado/val"

# Redimensionar imágenes en la carpeta "train"
print("Redimensionando imágenes en la carpeta train...")
redimensionar_imagenes(carpeta_train_entrada, carpeta_train_salida)

# Redimensionar imágenes en la carpeta "val"
print("\nRedimensionando imágenes en la carpeta val...")
redimensionar_imagenes(carpeta_val_entrada, carpeta_val_salida)

print("\nProceso completado.")
