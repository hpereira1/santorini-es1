from .Construtor import Construtor
class Jogador:
    def __init__(self):
        self._turno = False
        self._construtores = [Construtor(), Construtor()]
        self._vencedor = False
        self._perdedor = False
        self._simbolo = None
        self._nome = ''

    def initialize(self, aName, aSymbol):
        self._simbolo = aSymbol	#int
        self._nome = aName		#string
        for construtor in self._construtores:
            construtor.set_simbolo(aSymbol)
            print(construtor.get_simbolo())
            print(construtor.get_coordenada_xyz())
        self._turno = False		#bool
        self._vencedor = False		#bool
        self._perdedor = False		#bool
  
    def habilitar(self):
        self._turno = True

    def desabilitar(self):
        self._turno = False

    def resetar(self):
        self._vencedor = False
        self._perdedor = False
        self._turno = False
        for construtor in self._construtores:
            construtor.set_coordenada_xyz([-1, -1, -1])
            print(construtor.get_simbolo())
            print(construtor.get_coordenada_xyz())

    def get_vencedor(self):
        return self._vencedor

    def get_perdedor(self):
        return self._perdedor

    def get_turno(self):
        return self._turno

    def set_vencedor(self):
        self._vencedor = True

    def set_perdedor(self, perdedor):
        self._perdedor = perdedor

    def set_simbolo(self, simbolo):
        self._simbolo = simbolo
        
    def get_simbolo(self):
        return self._simbolo
    
    def set_turno(self, turno):
        self._turno = turno

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_construtores(self):
        return self._construtores

    def set_construtores(self, construtores):
        self._construtores = construtores

    def todos_builders_posicionados(self):
        for construtor in self._construtores:
            if not construtor.posicionado():
                return False
        return True

    def get_construtor_marcado(self):
        """Retorna o construtor marcado, se houver."""
        for construtor in self._construtores:
            if construtor.get_marcado():
                return construtor
        return None
