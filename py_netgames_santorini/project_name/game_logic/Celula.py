#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Jogador import Jogador
from Tabuleiro import Tabuleiro
from Construtor import Construtor
from  Entidade import Entidade
from typing import List

class Celula(Entidade):  # Substituir Entidade pela classe pai apropriada
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai, se necessário
        self._ocupante = None  # Inicializa ocupante como None

    def empty(self):
        self._ocupante = None

    def ocupado(self):
        return self._ocupante is not None

    def set_ocupante(self, construtor):
        self._ocupante = construtor

    def get_ocupante(self):
        return self._ocupante


