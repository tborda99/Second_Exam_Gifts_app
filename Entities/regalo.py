class Regalo():
    
    def __init__(self, amigo):
        self._amigo = amigo
        self._regalos =[]
    
    #GETTERS

    @property
    def amigo(self):
        return self._amigo
    
    @property
    def regalos(self):
        return self._regalos