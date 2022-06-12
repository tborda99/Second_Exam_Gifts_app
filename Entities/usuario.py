class Usuario():

    def __init__(self,cedula,nombre,telefono):
        self._cedula = cedula
        self._nombre = nombre
        self._telefono = telefono
        self._regalos =[] #los que regalo [[regalo,cedula a quien regalo],[regalo,cedula a quien regalo]]
        self._listaDeseos = [] #Los que quiero que me regalen
        self._deseos_satisfechos = [] #Los que quiero y ya me regalaron :)

    #GETTERS
    @property
    def cedula(self):
        return self._cedula
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono
    
    @property
    def regalos(self):
        return self._regalos

    @property
    def listaDeseos(self):
        return self._listaDeseos
    
    @property
    def deseos_satisfechos(self):
        return self._deseos_satisfechos