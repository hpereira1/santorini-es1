class Movimento:
    def __init__(self, linha : int, coluna: int):
        self._linha = linha
        self._coluna = coluna

    def get_linha(self):
        return self._linha

    def get_coluna(self):
        return self._coluna
