import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

numcaracteres = 0
dcaracteres = {}
def a():
    ruta=tkinter.filedialog.askopenfile(mode='r')
    abrir(numcaracteres, dcaracteres, ruta)


def abrir(numcaracteres, dcaracteres, ruta):
    with ruta as fichero:
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

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Button(frm, text="abrir archivo", command=a).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
root.mainloop()
