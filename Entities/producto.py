from abc import ABC, abstractmethod

class Producto(ABC):

    def __init__(self,nombre, precio_promedio):
        
        self._nombre = nombre
        self._precio_promedio = precio_promedio


    #GETTERS

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_promedio(self):
        return self._precio_promedio


    @abstractmethod
    def metodo_abstracto():
        pass