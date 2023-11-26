class BoardImage:
    def __init__(self):
        self._status_partida = 0
        self._message = ""  
        self._map = [[[0, 0] for _ in range(5)] for _ in range(5)]

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def get_value(self, linha, coluna):
        valor = self._map[linha][coluna]
        # print(f"Valor em get_value({linha}, {coluna}): {valor}")  # Para depuração
        return valor
    def set_value(self, linha, coluna, z : int, value : int):
        self._map[linha][coluna] = [z, value]

    # Getter para status_partida
    def get_status_partida(self):
        return self._status_partida

    # Setter para status_partida
    def set_status_partida(self, status_partida):
        self._status_partida = status_partida
