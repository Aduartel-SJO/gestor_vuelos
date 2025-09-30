# Creamos el archivo llamado reservas.txt yle introducimos los datos
with open("reservas.txt", "w", encoding="utf-8") as f:
    f.write(f"12A, Juan Pérez, Economy\n14B, María López, Business\n21C, Carlos García, Economy")

#volvemos a abrir el archivo y cogemos las lineas y las metemos en una array
with open("reservas.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()
# creamos un contador para determinar cuantos pasajeros estan en la alta esfera 
countBussisnes = 0
#determinamos la palabra clave para saber si estan o son de la plebe
palabra = "Business"
#imprimimos por pantalla cuantas reservas hay
print(f"hay {len(contenido)} reservas" )
#hacemos un for para imprimir de forma decente el contenido
for i in contenido:
    print(i.strip())
    # sumamos el contador segun la palabra clave
    if i.count(palabra):
        countBussisnes +=1
        
# decimos cuantos ricachones hay
print("Hay " + str(countBussisnes) + " cliente/s en Busisness")

