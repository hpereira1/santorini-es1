#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Entidade:
    def __init__(self):
        self._coordenada_xyz = list  # Valor inicial padrão, ajuste conforme necessário
        self._id = 0  # Valor inicial padrão, ajuste conforme necessário

    # Setter para coordenada_xyz
    def set_coordenada_xyz(self, coordenada_xyz):
        self._coordenada_xyz = coordenada_xyz

    # Getter para coordenada_xyz
    def get_coordenada_xyz(self):
        return self._coordenada_xyz

    # Setter para id (se necessário, pois IDs são geralmente atribuídos e não alterados)
    def set_id(self, id):
        self._id = id

    # Getter para id
    def get_id(self):
        return self._id
