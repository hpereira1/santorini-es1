#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Movimento:
    def __init__(self, linha : int, coluna: int):
        self._linha = linha
        self._coluna = coluna

    # Getter para linha
    def get_linha(self):
        return self._linha

    # Getter para coluna
    def get_coluna(self):
        return self._coluna
