class Jogador:
    def __init__(self, aNome, simbolo, construtores):
        self._turno = False
        self._construtores = construtores
        self._vencedor = False
        self._perdedor = False
        self._simbolo = simbolo
        self._nome = aNome

    def habilitar(self):
        self._turno = True

    def desabilitar(self):
        self._turno = False

    def resetar(self):
        self._vencedor = False
        self._perdedor = False
        self._turno = False

    def get_vencedor(self):
        return self._vencedor

    def get_perdedor(self):
        return self._perdedor

    def get_turno(self):
        return self._turno

    def set_vencedor(self, vencedor):
        self._vencedor = vencedor

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
        # Lógica para retornar o construtor marcado
        # Retornar a instância do construtor marcado
        pass
