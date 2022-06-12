from Entities.producto import Producto

class Vestimenta(Producto):

    def __init__(self,nombre,precio_promedio,talle,color):
        super().__init__(nombre, precio_promedio)
        self._talle = talle
        self._color = color
    

    #GETTERS
    @property
    def talle(self):
        return self._talle
    
    @property
    def color(self):
        return self._color

    def metodo_abstracto():
        pass