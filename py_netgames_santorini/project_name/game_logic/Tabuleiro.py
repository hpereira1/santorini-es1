#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Celula import Celula
from Jogador import Jogador
from AtorJogador import AtorJogador
from BoardImage import BoardImage
from Movimento import Movimento
from Construtor import Construtor
from typing import List

#	Board matchStatus
# 1 - match not started (initial message)
# 2 - next player (match in progress)
# 3 - irregular move (match in progress)
# 4 - match with winner (match finished)
# 5 - match tied (match finished)

class Tabuleiro:
    def __init__(self):
        self._matriz = [[Celula() for _ in range(5)] for _ in range(5)]
        self._jogadores = [Jogador("Jogador local", 1), Jogador("Jogador remoto", 2)] 
        self._estado_jogada = 0
        self._status_partida = 0
        self._vencedor = None 


   
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

    # Getters e Setters
    def get_status(self):
        return self._status_partida

    def set_status(self, status):
        self._status_partida = status

    def get_celula(self, aMove):
        pass

    def get_jogador_habilitado(self):
        pass

    def get_jogador_desabilitado(self):
        pass

    def get_estado_jogada(self):
        return self._estado_jogada

    def set_estado_jogada(self, estado_jogada):
        self._estado_jogada = estado_jogada

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
