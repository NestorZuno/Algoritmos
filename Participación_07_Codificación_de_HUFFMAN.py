from tkinter import *  # Importa todos los símbolos del módulo tkinter
from tkinter import ttk  # Importa el submódulo ttk de tkinter
from tkinter import filedialog  # Importa el submódulo filedialog de tkinter
#from backend_huffman import HuffmanTree  # Importa la clase HuffmanTree del módulo backend_huffman

class InterfazHuffman:
    def __init__(self):
        # Crea una instancia de HuffmanTree, que se utilizará para la compresión y descompresión de archivos
        self.arbol_huffman = HuffmanTree()
        # Llama al método para crear la ventana principal
        self.ventana_principal()

    def ventana_principal(self):
        # Crea la ventana principal de la interfaz gráfica
        root = Tk()
        # Crea un marco en la ventana con un relleno de 100 píxeles
        frm = ttk.Frame(root, padding=100)
        frm.grid()  # Coloca el marco en la ventana utilizando la cuadrícula
        # Crea una etiqueta de texto en el marco con el texto "Ventana principal"
        ttk.Label(frm, text="Ventana principal").grid(column=0, row=0)
        # Crea un botón en el marco con el texto "Abrir archivo" y vincula la función mostrar_info_archivo al evento click
        ttk.Button(frm, text="Abrir archivo", command=self.mostrar_info_archivo).grid(column=0, row=1)
        # Crea un botón en el marco con el texto "Comprimir archivo" y vincula el método comprimir de arbol_huffman al evento click
        ttk.Button(frm, text="Comprimir archivo", command=root.destroy).grid(column=0, row=2)
        # Crea un botón en el marco con el texto "Descomprimir archivo" y vincula el método descomprimir de arbol_huffman al evento click
        ttk.Button(frm, text="Descomprimir archivo", command=root.destroy).grid(column=0, row=3)
        root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

    def mostrar_info_archivo(self):
        # Abre un cuadro de diálogo para que el usuario seleccione un archivo
        nombre_archivo = filedialog.askopenfilename()
        if nombre_archivo:  # Verifica si se seleccionó un archivo
            contenido = ""  # Inicializa una cadena para almacenar el contenido del archivo
            caracteres = 0  # Inicializa una variable para contar el número de caracteres en el archivo
            contar_caracteres = {}  # Inicializa un diccionario para almacenar el conteo de caracteres
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                # Lee el contenido del archivo y cuenta el número de caracteres
                contenido = archivo.read()
                caracteres = len(contenido)
                # Cuenta la frecuencia de cada carácter en el contenido del archivo utilizando la instancia de HuffmanTree
                contar_caracteres = self.arbol_huffman.contar_caracteres(contenido)
            
            # Crea una ventana secundaria para mostrar la información del archivo seleccionado
            ventana_info = Toplevel()
            ventana_info.title("Información del archivo")
            # Crea una etiqueta de texto para mostrar el contenido del archivo
            etiqueta_contenido = Label(ventana_info, text="Contenido del archivo:")
            etiqueta_contenido.pack()
            # Crea un widget Text para mostrar el contenido del archivo con un tamaño de 10 filas y 50 columnas
            texto_contenido = Text(ventana_info, height=10, width=50)
            texto_contenido.insert(END, contenido)  # Inserta el contenido del archivo en el widget Text
            texto_contenido.pack()
            # Crea una etiqueta de texto para mostrar el número de caracteres en el archivo
            etiqueta_caracteres = Label(ventana_info, text=f"Número de caracteres: {caracteres}")
            etiqueta_caracteres.pack()
            # Crea una etiqueta de texto para mostrar el conteo de caracteres
            etiqueta_conteo = Label(ventana_info, text="Conteo de caracteres:")
            etiqueta_conteo.pack()
            # Itera sobre el diccionario de conteo de caracteres y crea etiquetas para cada par letra-cantidad
            for letra, cantidad in contar_caracteres.items():
                etiqueta = Label(ventana_info, text=f"'{letra}': {cantidad}")
                etiqueta.pack()
class HuffmanTree:
    def __init__(self):
        self.raiz = None

    def contar_caracteres(self, contenido):
        contar_caracteres = {}
        for caracter in contenido:
            contar_caracteres[caracter] = contar_caracteres.get(caracter, 0) + 1
        return contar_caracteres
# Crea una instancia de InterfazHuffman, lo que inicia la aplicación
InterfazHuffman()
