class BoardImage:
    def __init__(self):
        self._message = ""  # String inicializada como vazia
        self._map = 0       # Inteiro inicializado como 0
        # Inicializações adicionais para status_partida ou outros atributos podem ser adicionadas aqui

    # Getter para message
    def get_message(self):
        return self._message

    # Setter para message
    def set_message(self, message):
        self._message = message

    # Método para obter um valor específico; a implementação depende da estrutura interna de 'map'
    def get_value(self, linha, coluna):
        # Implementação específica vai aqui
        pass

    # Método para definir um valor específico; a implementação depende da estrutura interna de 'map'
    def set_value(self, linha, coluna, z, value):
        # Implementação específica vai aqui
        pass

    # Getter para status_partida
    def get_status_partida(self):
        # Implementação específica vai aqui
        pass

    # Setter para status_partida
    def set_status_partida(self, status_partida):
        # Implementação específica vai aqui
        pass
