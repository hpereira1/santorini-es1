#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import os
from tkinter import messagebox
from Dominio_problema import Tabuleiro
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from Dominio_problema import BoardImage

class AtorJogador(PyNetgamesServerListener):
    def __init__(self):
        self.meuTabuleiro = None  # Substituir None pelo tipo apropriado
        self.mainJanela = None    # Substituir None pelo tipo apropriado
        self._server_proxy = None # Substituir None pelo tipo apropriado
        self._turno_local = False
        self._partida_id = ""
        self.root = tk.Tk()
        self.button = tk.Button(self.root)

    def click(self, linha, coluna):
        pass  # Implementação específica vai aqui

    def atualizar_interface_usuario(self, novo_estado):
        pass  # Implementação específica vai aqui

    def get_partida_id(self):
        return self._partida_id

    def set_partida_id(self, partida_id):
        self._partida_id = partida_id

    def habilitar_interface(self):
        pass  # Implementação específica vai aqui
   
    def desabilitar_interface(self):
        pass  # Implementação específica vai aqui

    def get_local_habilitado(self):
        return self._turno_local



    def receber_erro(self, error):
        pass  # Implementação específica vai aqui

    def receber_desconexao(self):
        pass  # Implementação específica vai aqui

    def receber_jogada(self, move):
        pass  # Implementação específica vai aqui

    def add_listener(self):
        pass  # Implementação específica vai aqui

    def enviar_conexao(self):
        pass  # Implementação específica vai aqui

    def receber_sucesso_conexao(self):
        pass  # Implementação específica vai aqui

    def enviar_partida(self):
        pass  # Implementação específica vai aqui

    def receber_partida(self, partida):
        pass  # Implementação específica vai aqui
