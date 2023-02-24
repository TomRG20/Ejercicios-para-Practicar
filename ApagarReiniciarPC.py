"""
    Programa: Prueba para Apagar/reiniciar o cambiar de sesión en Windows usando Python.
    Autor: Tomás
    Versión: 1.0
    Fecha: 24/02/23    
"""

import os
from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.geometry("400x200")
ventana.title("Asistente inicio...")
ventana.resizable(False, False) 
ventana.configure(background="#e2e2e2")

cabezera = Label(ventana, text="Apagar, Reiniciar y cambiar usuario...", font=('Calibri 14'))
cabezera.pack(pady=10)

# mis funciones de los botones
def Apagar():
    os.system("shutdown /s /t 0") # /s es para apagar el sistema, el 0 significa que se apaga inmediatamente al pulsar el boton.

def Reiniciar(): 
    os.system("shutdown /r /t 0") # /r es para reiniciar el sistema

def CambiarUsu():
    os.system("shutdown -l /t 1 /d [p]") # /l es para cerrar la sesion del usuario, el 1 es el tiempo (t) en segundos que tardará. 

""" Uso: shutdown [/i | /l | /s | /sg | /r | /g | /a | /p | /h | /e | /o] [/hybrid] [/soft] [/fw] [/f]
    [/m \\equipo][/t xxx][/d [p|u:]xx:yy [/c "comentario"]]

    Sin argumentos  Muestra la ayuda. Es lo mismo que escribir /?.
    /?              Muestra la ayuda. Es lo mismo que no especificar ninguna 
                    opción.
    /i              Muestra la interfaz gráfica de usuario (GUI).
               Debe ser la primera opción.
    /l              Cierra la sesión. No se puede utilizar con las opciones /m o /d.
    /s              Apaga el equipo.
    /sg        Apaga el equipo. En el próximo arranque, si el Inicio de sesión de reinicio automático
               está habilitado, inicia sesión y bloquea automáticamente el último usuario interactivo.
               Después de iniciar sesión, reinicia las aplicaciones registradas.
    /r         Apaga completamente el equipo y reinícialo.
    /g         Apaga por completo el equipo y lo reinicia. Una vez reiniciado el sistema,
               si el Inicio de sesión de reinicio automático está habilitado, inicia sesión
               y bloquea automáticamente el último usuario interactivo.
               Después de iniciar sesión, reinicia las aplicaciones registradas.
    /a         Anula el apagado del sistema.
               Solo se puede usar durante el período de tiempo de espera.
               Combinar con /fw para borrar cualquier opción de arranque pendiente para acceder al firmware.
    /p              Apaga el equipo local sin tiempo de espera ni advertencia.
               Se puede usar con las opciones /d y /f.
    /h         Hiberna el equipo local.
               Se puede usar con la opción /f.
    /hybrid         Realiza un apagado del equipo y lo prepara para un inicio rápido.
               Debe usarse con la opción /s.
    /fw        Combinar con una opción de apagado para que en el siguiente arranque se acceda a la
               interfaz de usuario de firmware.
    /e         Documenta la razón del apagado inesperado de un equipo.
    /o         Va al menú de opciones de arranque avanzadas y reinicia el equipo.
               Debe usarse con la opción /r.
    /m \\equipo Especifica el equipo de destino.
    /t xxx     Establece el período de tiempo de espera antes del apagado en xxx segundos.
               El intervalo válido es de 0 a 315360000 (10 años); el valor predeterminado es 30.
               Si el período de tiempo de espera es superior a 0, el parámetro /f es
               implícito.
    /c "comentario" Comentario acerca de la razón del reinicio o apagado.
               Se permiten 512 caracteres como máximo.
    /f         Fuerza el cierre de las aplicaciones en ejecución sin advertir previamente a los usuarios.
               El parámetro /f es implícito cuando se especifica un valor mayor que 0
               para el parámetro /t.
    /d [p|u:]xx:yy  Proporciona la razón del reinicio o apagado.
               p indica que el reinicio o el apagado está planeado.
               u indica que la razón está definida por el usuario.
               Si no se especifica p ni u, el reinicio o el apagado no estarán
               planeados.
               xx es el número de razón principal (entero positivo inferior a 256).
               yy es el número de razón secundario (entero positivo inferior a 65536).
 """


# mis botones
Button(ventana, text="Apagar", command=Apagar, font=('normal', 12), bg='red').pack()
Button(ventana, text="Reiniciar", command=Reiniciar, font=('normal', 12), bg='red').pack()
Button(ventana, text="Cambiar Usuario", command=CambiarUsu, font=('normal', 12), bg='green').pack()


mainloop()