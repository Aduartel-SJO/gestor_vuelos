from datetime import datetime
import os 
#contenido corrupto, lo he hecho asi para poder verlo comodamente y en multilinea
contenidos_corruptos = """12A, Juan Pérez, Economy, 
14B, ,Business, París
,Carlos García, Economy, Madrid
05D, Ana Sánchez, ,Londres
19E, Luis Gómez, Economy, París
08F, Sofía Vargas, Economy, Londres
"""
# Creamos el archivo llamado reservas_maestro.txt y le introducimos los datos
with open("reservas_maestro_con_errores.txt", "w", encoding="utf-8") as f:
    f.write(contenidos_corruptos)

contenido_archivos = {
    
    "reservas_madrid.txt": [],
    "reservas_londres.txt": [],
    "reservas_paris.txt": [],
    "registro_errores.log": []
}
contador_archivos = 0
#volvemos a abrir el archivo y cogemos las lineas y las metemos en una array
with open("reservas_maestro_con_errores.txt", "r", encoding="utf-8") as f:
    contenidos_reserva_corruptos = f.readlines()

for contenido in contenidos_reserva_corruptos:
    #separamos el contenido de la linea en campos y los asignamos a una variable ordenada
    campos = [c.strip() for c in contenido.split(",")]
    asiento, nombre, clase, destino = campos
    archivo = "registro_errores.log"

    if not os.path.exists(archivo):
        contador_archivos += 1 
        print("Se ha creado el archivo: "+ archivo)

    error = ""
    # Comprobaciones para ver que campo esta vacio
    if not destino:
        error = f"{str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}, {contenido}, Destino desconocido"
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(error)

    elif not asiento:
        error = f"{str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}, {contenido}, Asiento no identificado"
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(error)

    elif not nombre:
        error = f"{str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}, {contenido}, nombre del pasajero desconocido"
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(error)

    elif not clase:
        error = f"{str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}, {contenido}, clase del pasajero no encontrada"
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(error)
    # Si no hay ninguno se comprueba a que destino se dirijen y se clasifica
    else:
        if "Madrid" in destino:
            archivo = "reservas_madrid.txt"
        elif "Londres" in destino:
            archivo = "reservas_londres.txt"
        else:
            archivo = "reservas_paris.txt"

            # Miramos si el archivo no existe y le sumamos 1 al contador, ya que se creará proximamente
            if not os.path.exists(archivo):
                contador_archivos += 1 
                print("Se ha creado el archivo: "+ archivo)

            # Abrimos el archivo para escribir
            with open(archivo, "a+", encoding="utf-8") as f:
                f.write(contenido)
    if error == "":
        # guardamos la info en el diccionario 
        contenido_archivos[archivo].append(contenido)
    else:
        # guardamos la info en el diccionario 
        contenido_archivos[archivo].append(error)  

# imprimimos por pantalla los contenidos de cada archivo
for nombre_archivo, ca in contenido_archivos.items():
    if ca != []:
        print("contenido de " + nombre_archivo)
        for c in ca:
            print(c)