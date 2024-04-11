numcaracteres = 0
dcaracteres = {}

with open('Gullivers_Travels.txt', 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        for caracter in linea:
            if caracter != '\n':  # Excluir saltos de línea
                numcaracteres += 1
                dcaracteres[caracter] = dcaracteres.get(caracter, 0) + 1

# Ordenar el diccionario por valor (número de repeticiones)
dcaracteres_ordenado = sorted(dcaracteres.items(), key=lambda x: x[1], reverse=True)

# Escribir la información en un archivo de texto
with open('informacion_caracteres.txt', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write('El texto contiene %s caracteres (sin contar saltos de línea).\n\n' % numcaracteres)
    archivo_salida.write('Los caracteres se han repetido de la siguiente forma:\n')
    for caracter, repeticiones in dcaracteres_ordenado:
        veces = 'veces' if repeticiones > 1 else 'vez'
        archivo_salida.write('El caracter "%s" se ha repetido %s %s\n' % (caracter, repeticiones, veces))

print("La información se ha guardado en 'informacion_caracteres.txt'")
