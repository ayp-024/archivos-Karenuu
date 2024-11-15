with open(r'C:\Users\USUARIO\OneDrive - ITESO\ALGORITMOS Y PROGRAMACIÓN\archivos-Karenuu\data\calificaciones.txt', mode='r') as archivo:
    codigo = archivo.readlines()

# proceso
final = []

for i in codigo:  # Para leer cada linea del codigo
    i = i.strip()  # .strip() elimina los saltos de linea y los espacios en blanco
    lista = i.split()  # Lo convierte a lista
    nombre = lista[0]  # Coge el primer elemento
    apellido = lista[1]  # Coge el segundo elemento

    calificaciones = []

    for c in lista[2:]:
        calificaciones.append(int(c))  # Agrega cada calificación como un entero

    promedios = sum(calificaciones) / len(calificaciones)

    resultado = f'{apellido.upper()}, {nombre}: {round(promedios, 2)}'
    final.append(resultado)  # Guarda cada resultado en la lista final

# Guardar los resultados en el archivo
with open('promedio.txt', mode='w') as archivo_final:
    for linea in final:
        archivo_final.write(linea + '\n')

        



