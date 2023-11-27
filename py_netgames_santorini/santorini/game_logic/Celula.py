from .Jogador import Jogador
from .Construtor import Construtor
from  .Entidade import Entidade

class Celula(Entidade):  
    def __init__(self):
        super().__init__()  
        self._ocupante = None 

    def empty(self):
        self._ocupante = None

    def ocupado(self):
        return self._ocupante is not None

    def set_ocupante(self, construtor :Construtor):
        self._ocupante = construtor

    def get_ocupante(self):
        return self._ocupante


