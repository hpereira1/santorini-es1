class BoardImage:
    def __init__(self):
        self._status_partida = 0
        self._message = ""  
        self._map = []
        for y in range(5):
            line = []
            for x in range(5):
                line.append(0)
            self.map.append(line)

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def get_value(self, linha, coluna):
        return self.map[(linha-1)][(coluna-1)]

    def set_value(self, linha, coluna, z, value):
        self.map[(linha-1)][(coluna-1)] = (z, value)

    # Getter para status_partida
    def get_status_partida(self):
        return self._status_partida

    # Setter para status_partida
    def set_status_partida(self, status_partida):
        self._status_partida = status_partida
