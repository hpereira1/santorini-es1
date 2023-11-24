#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import os
from tkinter import messagebox
from Tabuleiro import Tabuleiro
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from BoardImage import BoardImage
from PIL import Image, ImageTk

class AtorJogador(PyNetgamesServerListener):
    def __init__(self):
        self.mainJanela = Tk()    
        self.mainJanela.title("Santorini")
        self._turno_local = False
        self._partida_id = ""

        self.mainWindow.resizable(False, False)
        self.board.geometry("500x500")
        self.grass_image1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png'))
        self.grass_image2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama2.png'))
        
        self.boardView = []
        for i in range(5):
            self.board.grid_rowconfigure(i, weight=1)
            row = []
            for j in range(5):
                self.board.grid_columnconfigure(j, weight=1)
                grass_image = self.grass_image1 if (i + j) % 2 == 0 else self.grass_image2
                label = Label(self.board, image=grass_image)
                label.image = grass_image
                label.grid(row=i, column=j, sticky='news')
                label.bind('<Button-1>', lambda event, i=i, j=j: self.click(event, i, j))
                row.append(label)
            self.boardView.append(row)

        self.labelMessage = Label(self.messageFrame, bg="gray", text='Aguardando início de partida', font="arial 14")
        self.labelMessage.grid(row=0, column=0, columnspan=3)
        self.mainFrame.grid(row=0 , column=0)
        self.messageFrame.grid(row=1 , column=0) 

        self.meuTabuleiro = Tabuleiro()
        self.disable_interface()
        self.set_partida_id('')

        self.add_listener()	# Pyng use case "add listener"
        self.send_connection()	# Pyng use case "send connect"

        self.mainWindow.mainloop()

    def click(self, event, linha, coluna):
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
        messagebox.showinfo(message='Notificação de erro do servidor. Feche o programa.')       

    def receber_desconexao(self):
        pass  # Implementação específica vai aqui

    def receber_jogada(self, move):
        pass  # Implementação específica vai aqui

    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)

    def enviar_conexao(self):
        self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

    def receber_sucesso_conexao(self):
        messagebox.showinfo(message='Conectado ao servidor') 
        self.send_match(2)

    def enviar_partida(self, ):
        self.server_proxy.send_match(2) 

    def receber_partida(self, partida):
        messagebox.showinfo(message='Partida iniciada') 
        print('********** ORDEM: ', partida.position)
        print('********** match_id: ', partida.match_id)
        self.set_partida_id(partida.match_id)
        if (match.position == 1):
            self.enable_interface()
        self.myBoard.startMatch(self.get_local_enabled())
        new_state = self.myBoard.getState()
        self.update_user_interface(new_state)

