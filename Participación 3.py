import tkinter as tk

# Crear una instancia de la clase Tk
ventana = tk.Tk()

# Configurar el título de la ventana
ventana.title("Mi Ventana Tkinter")

# Definir las dimensiones de la ventana
ventana.geometry("800x600")

# Crear una etiqueta para mostrar el mensaje
label = tk.Label(ventana, text="¡ventana de prueba!")
label.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
