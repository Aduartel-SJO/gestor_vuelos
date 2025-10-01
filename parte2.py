import os

# Creamos el archivo llamado reservas_maestro.txt y le introducimos los datos
with open("reservas_maestro.txt", "w", encoding="utf-8") as f:
    f.write(f"12A, Juan Pérez, Economy, Madrid\n14B, María López, Business, París\n21C, Carlos García, Economy, Madrid\n05D, Ana Sánchez, Business, Londres\n19E, Luis Gómez, Economy, París\n08F, Sofía Vargas, Economy, Londres\n")

#volvemos a abrir el archivo y cogemos las lineas y las metemos en una array
with open("reservas_maestro.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

#creamos un diccionario que tendrá los contenidos
contenido_archivos = {
    "reservas_madrid.txt": [],
    "reservas_londres.txt": [],
    "reservas_paris.txt": []
}
#un contador para ver cuantos archivos se han creado
contador_archivos = 0
#bucle para escribir las reservas a su archivo correspondiente y contar archivos creados
for c in contenido:
    if "Madrid" in c:
        archivo = "reservas_madrid.txt"
    elif "Londres" in c:
        archivo = "reservas_londres.txt"
    else:
        archivo = "reservas_paris.txt"

    # Miramos si el archivo no existe y le sumamos 1 al contador, ya que se creará proximamente
    if not os.path.exists(archivo):
        contador_archivos += 1 
        print("Se ha creado el archivo: "+ archivo)

    # Abrimos el archivo para escribir
    with open(archivo, "a+", encoding="utf-8") as f:
        f.write(c)
    # guardamos la info en el diccionario 
    contenido_archivos[archivo].append(c)



# imprimimos por pantalla los contenidos de cada archivo
for nombre, ca in contenido_archivos.items():
    print("contenido de " + nombre)
    for c in ca:
        print(c)
        



