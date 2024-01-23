import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import panas as pd

def cargar_imagen(url):
    try:
        imagen_respuesta = requests.get(url)
        imagen_respuesta.raise_for_status()

        imagen_pil = Image.open(BytesIO(imagen_respuesta.content))
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        label_imagen.config(image=imagen_tk)
        label_imagen.image = imagen_tk
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

def mostrar_historia(texto_historia, opciones):
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, texto_historia)
    crear_botones_opciones(opciones)

def crear_botones_opciones(opciones):
    for boton in botones_opciones:
        boton.destroy()
    botones_opciones.clear()
    for opcion_texto, opcion_accion, *resto_opcion in opciones:
        if resto_opcion:  # Verifica si hay más elementos en la tupla
            url_imagen = resto_opcion[0]
            boton = tk.Button(root, text=opcion_texto, command=lambda url=url_imagen: opcion_accion(url), fg="white", bg="black", font=("Arial", 16))
        else:
            boton = tk.Button(root, text=opcion_texto, command=opcion_accion, fg="white", bg="black", font=("Arial", 16))
        boton.pack(side="top", pady=5)
        botones_opciones.append(boton)

def iniciar_historia():
    imagen_inicial_url = "https://i.ibb.co/Vpz212K/images.jpg"  # Reemplaza esto con la URL de tu imagen inicial
    cargar_imagen(imagen_inicial_url)  # Carga la imagen inicial
    historia_inicial = "Eres un explorador en busca de tesoros. Encuentras dos caminos. ¿Cuál eliges?"
  
    opciones = [
        ("Tomar el camino a la izquierda", continuar_historia_izquierda),
        ("Tomar el camino a la derecha", continuar_historia_derecha)
    ]

    mostrar_historia(historia_inicial, opciones)
    
    
def continuar_historia_izquierda(url_imagen=None): #variable
    nueva_historia = "Encuentras un cofre con monedas de oro."
    
    opciones = [
        ("Abrir el cofre", finalizar_historia_exito),
        ("Dejar el cofre y seguir explorando", finalizar_historia_explorando)
    ]
    cargar_imagen(url_imagen) if url_imagen else None
    mostrar_historia(nueva_historia, opciones)
    
def continuar_historia_derecha(url_imagen=None):
    nueva_historia = "Te pierdes en el bosque. Fin de la historia."
    opciones = []
    cargar_imagen(url_imagen) if url_imagen else None
    mostrar_historia(nueva_historia, opciones)
    
def finalizar_historia_exito(url_imagen=None):
    nueva_historia = "¡Felicidades! Encontraste un tesoro valioso."
    opciones = []
    cargar_imagen(url_imagen) if url_imagen else None
    mostrar_historia(nueva_historia, opciones)

def finalizar_historia_explorando(url_imagen=None):
    nueva_historia = "Decides seguir explorando. Fin de la historia."
    opciones = []
    cargar_imagen(url_imagen) if url_imagen else None
    mostrar_historia(nueva_historia, opciones)

# Crear la ventana principal
root = tk.Tk()
root.title("Historia Interactiva")
root.geometry("800x600")

# Crear widgets
label_imagen = tk.Label(root)
label_imagen.pack()

texto = tk.Text(root, wrap="word", width=80, height=10, font=("Arial", 14), padx=10, pady=10)
texto.pack()

botones_opciones = []

# Iniciar la historia
iniciar_historia()

# Bucle principal de la interfaz gráfica
root.mainloop()



