#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Celula import Celula
from .Jogador import Jogador
from .BoardImage import BoardImage
from .Movimento import Movimento
from .Construtor import Construtor   

#	Board matchStatus
# 1 - match not started (initial message)
# 2 - next player (match in progress)
# 3 - irregular move (match in progress)
# 4 - match with winner (match finished)
# 5 - match tied (match finished)

class Tabuleiro:
    def __init__(self):
        self._matriz = []
        for x in range(5):
            linha = []
            for y in range(5):
                celula = Celula()
                celula.set_coordenada_xyz([x, y, 0])
                linha.append(celula)
            self._matriz.append(linha)
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
        self._matriz = []
        for x in range(5):
            linha = []
            for y in range(5):
                celula = Celula()
                celula.set_coordenada_xyz([x, y, 0])
                linha.append(celula)
            self._matriz.append(linha)
        self._jogadores[0].resetar()
        self._jogadores[1].resetar()
        self.set_status(0)

    def get_estado(self):
        estado = BoardImage()
        estado.set_status_partida(self.get_status())
        if (self.get_status() == 0): 
            estado.set_message("Aguardando início de partida")
        elif (self.get_status() == 1):
            estado.set_message("fase inicial: " + (self.get_jogador_habilitado()).get_nome() + " deve jogar")	
        elif (self.get_status() == 2): 
            estado.set_message((self.get_jogador_habilitado()).get_nome() + " deve jogar")
        elif (self.get_status() == 3): 
            estado.setMessage("jogada irregular - jogue novamente")
        elif (self.get_status() == 4): 
            estado.set_message((self.get_vencedor()).get_nome() + " venceu a partida")
        for x in range(3):
            for y in range(3):
                cel = self._matriz[x][y]
                if (cel.ocupado()):
                    value = (cel.get_ocupante()).get_simbolo()	
                else:
                    value = 0
                z = cel.get_coordenada_xyz()[2]
                estado.set_value((x+1), (y+1),z, value)
        return estado

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
        if (self._jogadores[0].get_vencedor()):
            return self._jogadores[0]
        else:
            if (self._jogadores[1].get_vencedor()):
                return self._jogadores[1]
            else:
                return None	

    def set_vencedor(self, vencedor):
        self._vencedor = vencedor
