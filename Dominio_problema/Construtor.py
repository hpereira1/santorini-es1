#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_problema import Jogador
from Dominio_problema import Entidade
from typing import List

class Construtor(Entidade):  # Substituir Entidade pela classe pai apropriada
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai, se necessário
        self._marcado = False  # Inicializa marcado como False

    def set_marcado(self, marcado):
        self._marcado = marcado

    def get_marcado(self):
        return self._marcado

    def construtor_liberado(self):
        # Lógica para verificar se o construtor está liberado
        # Retornar True ou False dependendo da condição
        pass
