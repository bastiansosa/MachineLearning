import os

def cambiar_nombres_carpeta(ruta_carpeta):
    # Obtener la lista de archivos en la carpeta
    lista_archivos = os.listdir(ruta_carpeta)
    cantidad_imagenes = len(lista_archivos)
    
    # Verificar si hay más de 100 archivos
    if cantidad_imagenes > 100:
        print("La cantidad de imágenes excede 100. No se realizarán cambios.")
        return
    
    # Recorrer cada archivo en la lista
    for i, nombre_archivo in enumerate(lista_archivos):
        ruta_actual = os.path.join(ruta_carpeta, nombre_archivo)
        
        if os.path.isfile(ruta_actual):  # Verificar si es un archivo
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(nombre_archivo)
            
            # Nuevo nombre para el archivo
            nuevo_nombre = str(i+76) + extension
            
            # Ruta destino con el nuevo nombre
            ruta_destino = os.path.join(ruta_carpeta, nuevo_nombre)
            
            # Cambiar el nombre del archivo
            os.rename(ruta_actual, ruta_destino)
            print(f"Se cambió el nombre de '{nombre_archivo}' a '{nuevo_nombre}'.")
            
            # Detener el proceso al llegar al número 100
            if i >= 99:
                break

# Ejemplo de uso
ruta_carpeta = "C:/Users/bastian/Desktop/d/"  # Reemplaza con la ruta de tu carpeta
cambiar_nombres_carpeta(ruta_carpeta)
