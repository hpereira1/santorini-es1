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
        self._jogadores = [Jogador("Jogador local", 1, [Construtor(1), Construtor(1)]), Jogador("Jogador remoto", 2, [Construtor(2), Construtor(2)])] 
        self._estado_jogada = 0
        self._status_partida = 0
        self._vencedor = None 


   
    def click(self, linha, coluna):
        jogada_a_enviar = {}
        status = self.get_status()
        if (status==1 or status==2 or status==3):
            aMove = Movimento(linha, coluna)
            self.processar_jogada(aMove)
            if (self._status_partida!=3):
                jogada_a_enviar['linha']=str(linha)
                jogada_a_enviar['coluna']=str(coluna)
        return jogada_a_enviar

    def start_partida(self, turno_local):
        self.resetar()
        self.set_status(1)
        if turno_local:
            self._jogadores[0].habilitar()
        else:
            self._jogadores[1].habilitar()
            self.invert_player_symbol()

    def todos_construtores_posicionados(self):
        # Retorna True se todos os construtores dos dois jogadores estiverem posicionados
        return (self._jogadores[0].todos_builders_posicionados() and 
                self._jogadores[1].todos_builders_posicionados())
        
    def processar_jogada(self, aMove : Movimento):
        celula_selecionada = self.get_celula(aMove)
        status = self.get_status()
        if not (self.todos_construtores_posicionados() )or ((status == 3 and not self.todos_construtores_posicionados())):
            self.inicio_de_jogo(celula_selecionada)
            self.set_status(1)
        else:
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

    def invert_player_symbol(self):	
        aux1 = self._jogadores[0].get_simbolo()
        aux2 = self._jogadores[1].get_simbolo()
        self._jogadores[0].set_simbolo(aux2)
        self._jogadores[1].set_simbolo(aux1)
        
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
            estado.set_message("jogada irregular - jogue novamente")
        elif (self.get_status() == 4): 
            estado.set_message((self.get_vencedor()).get_nome() + " venceu a partida")
        for x in range(5):
            for y in range(5):
                # celula = self._matriz[x][y]
                # z = celula.get_coordenada_xyz()[2]
                # value = celula.get_ocupante().get_simbolo() if celula.ocupado() else 0
                
                # estado.set_value(x + 1, y + 1, z, value)
                cel = self._matriz[x][y]
                value = 0  # Inicializa value
                z = cel.get_coordenada_xyz()[2]
                # print(f"val z = {z}")
                if (cel.ocupado()):
                    ocupante = cel.get_ocupante()
                    # print(f"Celula ({x}, {y}) está ocupada pelo construtor com símbolo {ocupante.get_simbolo()}")
                    if isinstance(ocupante,Construtor):
                        value = ocupante.get_simbolo()	
                        # print(f"val value = {value}")       
                # else:
                #     print(f"Celula ({x}, {y}) está vazia")
                estado.set_value((x+1), (y+1),z, value)
                print(estado.get_value(x,y))
        return estado

    # Getters e Setters
    def get_status(self):
        return self._status_partida

    def set_status(self, status):
        self._status_partida = status

    def get_celula(self, aMove : Movimento):
        linha = aMove.get_linha()
        coluna = aMove.get_coluna()
        if 0 <= linha < len(self._matriz) and 0 <= coluna < len(self._matriz[0]):
            return self._matriz[linha][coluna]
        else:
            return None


    def get_jogador_habilitado(self):
        if self._jogadores[0].get_turno():
            return self._jogadores[0]
        else: 
            return self._jogadores[1]

    def get_jogador_desabilitado(self):
        if self._jogadores[0].get_turno():
            return self._jogadores[1]
        else: 
            return self._jogadores[0]

    def get_estado_jogada(self):
        return self._estado_jogada

    def set_estado_jogada(self, estado_jogada):
        self._estado_jogada = estado_jogada

    def inicio_de_jogo(self, celula_selecionada : Celula):
        jogador_habilitado = self.get_jogador_habilitado() 
        jogador_desabilitado = self.get_jogador_desabilitado()
        construtores = jogador_habilitado.get_construtores()
        coord_cell = celula_selecionada.get_coordenada_xyz()
        if (celula_selecionada.ocupado()):
            self.set_status(3)
            return
        else: 
            for construtor in construtores:
                if not construtor.posicionado():
                    celula_selecionada.set_ocupante(construtor)
                    construtor.set_coordenada_xyz(coord_cell)
                    break
            
        if(jogador_habilitado.todos_builders_posicionados()):
            jogador_habilitado.set_turno(False)
            jogador_desabilitado.set_turno(True)
            self.set_status(1)
            
            if(jogador_desabilitado.todos_builders_posicionados()):
                self.set_status(2)
                print(self.get_status())
                
            
    def selecionar_construtor(self, celula_selecionada : Celula):
        pass

    def construir(self, celula_selecionada : Celula):
        pass

    def checar_adjacencia(self, celula_selecionada : Celula):
        pass

    def movimentar_construtor(self, celula_selecionada : Celula):
        pass

    def avaliar_perdedor(self, celula_selecionada : Celula):
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
