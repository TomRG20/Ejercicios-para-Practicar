import time
import winsound
import win10toast  #Esta libreria la he tenido que instalar desde la consola

def dormir():
    time.sleep(2)
    winsound.Beep(frequency = 250, duration = 2)

def notificador(mensaje, minutos):
    notificator = win10toast.ToastNotifier()
       
    notificator.show_toast("TomiKode", f"Prepárate en {minutos} minutos...", duration = 3)
    dormir()
    notificator.show_toast(f"¡Alarma!", mensaje, duration = 3)
    dormir()
    notificator.show_toast("Python","Hello World", duration = 10)
    
    notificator.show_toast("Hello World!!!", "Python is 10 seconds awsm!", icon_path = "custom.ico", duration = 10)
    
if __name__ == "__main__":
    mensaje ="Hola"
    minutos = 1
    notificador(mensaje, minutos)
