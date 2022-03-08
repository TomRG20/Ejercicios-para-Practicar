
class Lavadora: 
    
    def __init__(self):
        pass
    
    #metodo publico lavar
    def lavar(self, temperatura = 'caliente'):
        #metodos privados de la clase se pone _ delente del nombre
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')    
    def _anadir_jabon(self):
        print('Añadiendo jabon')        
    def _lavar(self):
        print('Lavando la ropa')
    def _centrifugar(self): 
        print('Centrifugando la ropa')
    
if __name__ == '__main__':   #si este archivo se ejecuta directamente este es el punto de entrada
    lavadora = Lavadora()
    lavadora.lavar()