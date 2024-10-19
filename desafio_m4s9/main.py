#ejercicio m4s9 -Daniela Miranda

def crear_archivo():
    # Abri el archivo en modo escritura (si no existe, se crea) con codificación UTF-8
    with open('informacion.dat', 'w', encoding='utf-8') as archivo:
        # Imprime las 1eras líneas 
        archivo.write("Hola Mundo\n")
        archivo.write("Este en una nueva línea en el archivo agregando\n")
        archivo.write("la segunda línea del archivo finalizando la línea agregada\n\n")

        # Añadir las líneas con datos de procesamiento
        for i in range(1, 6):
            archivo.write(f"Datos de Procesamiento en la línea {i}\n")
        
        # Imprime la última línea
        archivo.write("Este en una nueva línea en el archivo agregando la segunda línea del archivo finalizando la línea agregada\n")

    print("El archivo ha sido creado y se ha agregado el contenido correctamente.")

def reemplazar_contenido(archivo):
    # Contador de reemplazos
    contador_reemplazos = 0
    
    # contenido del archivo
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.readlines()
    
    # Reemplaza "Información" por "Procesamiento" y los cuenta
    for i in range(len(contenido)):
        reemplazos = contenido[i].count("Información")
        contador_reemplazos += reemplazos
        contenido[i] = contenido[i].replace("Información", "Procesamiento")
    
    # Escribir contenido modificado
    with open(archivo, 'w', encoding='utf-8') as file:
        file.writelines(contenido)

    return contador_reemplazos

# Crear el archivo
crear_archivo()

# Ruta del archivo
nombre_archivo = 'informacion.dat'

# Llamar a la función de reemplazo y obtener el número de reemplazos
num_reemplazos = reemplazar_contenido(nombre_archivo)

# Imprimir el resultado
print(f"Se realizaron: {num_reemplazos} reemplazos")

# Verificar el contenido final del archivo (opcional)
with open(nombre_archivo, 'r', encoding='utf-8') as file:
    print("\nContenido final del archivo:")
    print(file.read())
