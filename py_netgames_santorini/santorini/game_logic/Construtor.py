#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Jogador import Jogador
from .Entidade import Entidade

class Construtor(Entidade):  # Substituir Entidade pela classe pai apropriada
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai, se necessário
        self._marcado = False  # Inicializa marcado como False
        self._coordenada_xyz = [-1, -1, -1]
        self._simbolo = 0
        
    def set_marcado(self, marcado):
        self._marcado = marcado

    def get_marcado(self):
        return self._marcado

    def construtor_liberado(self):
        # Lógica para verificar se o construtor está liberado
        # Retornar True ou False dependendo da condição
        pass
    
    def posicionado(self):
        return self._coordenada_xyz != [-1, -1, -1]
    
    def set_simbolo(self, simbolo):
        self._simbolo = simbolo
        
    def get_simbolo(self):
        return self._simbolo