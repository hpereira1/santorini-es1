#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_problema import Celula
from Dominio_problema import Jogador
from Dominio_problema import AtorJogador
from Dominio_problema import BoardImage
from Dominio_problema import Movimento
from Dominio_problema import Construtor
from typing import List

#	Board matchStatus
# 1 - match not started (initial message)
# 2 - next player (match in progress)
# 3 - irregular move (match in progress)
# 4 - match with winner (match finished)
# 5 - match tied (match finished)

class Tabuleiro:
    def __init__(self):
        self.matriz = None  # Substituir None pelo tipo apropriado
        self.jogadores = None  # Substituir None pelo tipo apropriado
        self.estado_jogada = 0
        self.status_partida = 0
        self._vencedor = None  # Substituir None pelo tipo apropriado

    # Implementações dos métodos (os corpos dos métodos estão vazios, precisam ser preenchidos)

    def tabuleiro(self):
        pass

    def click(self, linha, coluna):
        pass

    def start_partida(self, turno_local):
        pass

    def processar_jogada(self, aMove):
        pass

    def resetar(self):
        pass

    def get_estado(self):
        pass

    def get_status(self):
        return self.status_partida

    def set_status(self, status):
        self.status_partida = status

    def get_celula(self, aMove):
        pass

    def get_jogador_habilitado(self):
        pass

    def get_jogador_desabilitado(self):
        pass

    def get_estado_jogada(self):
        return self.estado_jogada

    def set_estado_jogada(self, estado_jogada):
        self.estado_jogada = estado_jogada

    def inicio_de_jogo(self, celula_selecionada):
        pass

    def selecionar_construtor(self, celula_selecionada):
        pass

    def construir(self, celula_selecionada):
        pass

    def checar_adjacencia(self, celula_selecionada):
        pass

    def movimentar_construtor(self, celula_selecionada):
        pass

    def avaliar_perdedor(self, celula_selecionada):
        pass

    def get_vencedor(self):
        return self._vencedor

    def set_vencedor(self, vencedor):
        self._vencedor = vencedor

