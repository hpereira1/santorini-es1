from .Entidade import Entidade

class Construtor(Entidade):
    def __init__(self):
        super().__init__() 
        self._marcado = False
        self._coordenada_xyz = [-1, -1, -1]
        self._simbolo = None
        
    def set_marcado(self, marcado):
        self._marcado = marcado

    def get_marcado(self):
        return self._marcado
    
    def posicionado(self):
        return self._coordenada_xyz != [-1, -1, -1]
    
    def set_simbolo(self, simbolo):
        self._simbolo = simbolo
        
    def get_simbolo(self):
        return self._simbolo