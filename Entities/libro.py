from Entities.producto import Producto

class Libro(Producto):

    def __init__(self,nombre,precio_promedio,autores):
        super().__init__(nombre, precio_promedio)
        self._autores = autores
    

    #GETTERS
    @property
    def autores(self):
        return self._autores

    def metodo_abstracto():
        pass