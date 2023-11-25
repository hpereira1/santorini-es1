#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import os
from tkinter import messagebox
from .Tabuleiro import Tabuleiro
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from .BoardImage import BoardImage
from PIL import Image, ImageTk

class AtorJogador(PyNetgamesServerListener):
    def __init__(self):
        self.mainJanela = Tk()
        self.mainJanela.configure(bg='darkgray')
        self.mainJanela.title("Santorini")
        self._turno_local = False
        self._partida_id = ""

        self.mainJanela.geometry("800x600")
        self.mainJanela.resizable(False, False)
        self.mainJanela.grid_rowconfigure(0, weight=1)
        self.mainJanela.grid_columnconfigure(0, weight=1)
        
        self.mainFrame = Frame(self.mainJanela, bg="gray")
        self.mainFrame.grid(row=0, column=0, sticky="nsew", padx=44, pady=40)
        
        self.messageFrame = Frame(self.mainJanela, bg="gray")
        self.messageFrame.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        # self.mainFrame = Frame(self.mainJanela, padx=44, pady=40, bg="gray")
        # self.messageFrame = Frame(self.mainJanela, padx=4, pady=4, bg="gray")

        # self.mainFrame.grid(row=0 , column=0)
        # self.messageFrame.grid(row=1 , column=0) 
        # self.mainFrame.grid(row=0, column=0, sticky="nsew")
        # self.messageFrame.grid(row=1, column=0, sticky="ew")
        # self.grass_image1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png'))
        # self.grass_image2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama2.png'))
        
        self.boardView = []
        for i in range(5):
            self.mainFrame.grid_rowconfigure(i, weight=1)
            self.mainFrame.grid_columnconfigure(i, weight=1)
            self.grass_image1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png'))
            self.grass_image = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama2.png'))
            self.andar1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Andar1.png'))
            self.andar2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Andar2.png'))
            self.andar3 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Andar3.png'))
            self.andar4 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Andar4.png'))
        
        self.boardView = []
        for i in range(5):
            row = []
            for j in range(5):
                # grass_image = self.grass_image1 if (i + j) % 2 == 0 else self.grass_image2
                label = Label(self.mainFrame, image=self.grass_image, bd = 2, relief="solid")
                label.image = self.grass_image
                label.grid(row=i, column=j, sticky='news')
                label.bind('<Button-1>', lambda event, i=i, j=j: self.click(event, i, j))
                row.append(label)
            self.boardView.append(row)

        self.labelMessage = Label(self.messageFrame, text='Aguardando início de partida', font="arial 14")
        self.labelMessage.pack(fill="x")
        # self.labelMessage = Label(self.messageFrame, bg="gray", text='Aguardando início de partida', font="arial 14")
        # self.labelMessage.grid(row=0, column=0, columnspan=3)


        self.meuTabuleiro = Tabuleiro()
        self.desabilitar_interface()
        self.set_partida_id('')

        self.add_listener()	# Pyng use case "add listener"
        self.enviar_conexao()	# Pyng use case "send connect"

        self.mainJanela.mainloop()
        

    
    def click(self, event, linha, coluna):
        if (self.get_local_habilitado()):
            jogada_a_enviar = self.meuTabuleiro.click(linha, coluna)
            novo_estado = self.meuTabuleiro.get_estado()
            self.atualizar_interface_usuario(novo_estado)
            if (bool(jogada_a_enviar)):
                self.desabilitar_interface()
                self.server_proxy.send_move(self.get_partida_id(), jogada_a_enviar)
        else:
            messagebox.showinfo(message='Você não está habilitado para jogar')


    def atualizar_interface_usuario(self, novo_estado : BoardImage):
        self.labelMessage['text']=novo_estado.get_message()
        for x in range(5):
            for y in range(5):
                label = self.boardView[x][y]
                dados_cel = novo_estado.get_value(x+1, y+1)
                if dados_cel[1]==0: # n ocupado
                    if dados_cel[0] == 0:
                        label['imag'] = self.grass_image
                    elif dados_cel[0] == 1:
                        label['imag'] = self.andar1
                    elif dados_cel[0] == 2:
                        label['imag'] = self.andar2
                    elif dados_cel[0] == 3:
                        label['imag'] = self.andar3
                    elif dados_cel[0] == 4:
                        label['imag'] = self.andar4
                    
                elif dados_cel[1]==1: #ocupado jog1
                    pass
                    
                elif dados_cel[1]==2: #ocupado jog2
                    pass
                    
    def get_partida_id(self):
        return self._partida_id

    def set_partida_id(self, partida_id):
        self._partida_id = partida_id

    def habilitar_interface(self):
        self._turno_local = True
   
    def desabilitar_interface(self):
        self._turno_local = False

    def get_local_habilitado(self):
        return self._turno_local



    def receive_error(self, error):
        messagebox.showinfo(message='Notificação de erro do servidor. Feche o programa.')       

    def receive_disconnect(self):
        messagebox.showinfo(message='Desconectado do servidor')
        self.meuTabuleiro.resetar()
        novo_estado = self.meuTabuleiro.get_estado()
        self.atualizar_interface_usuario(novo_estado)
        self.enviar_conexao()	

    def receive_move(self, move):
        received_move = move.payload
        self.meuTabuleiro.click(int(received_move['linha']), int(received_move['coluna']))
        novo_estado = self.meuTabuleiro.get_estado()
        self.atualizar_interface_usuario(novo_estado)
        if (novo_estado.get_() == 2):
            self.enable_interface()

    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)

    def enviar_conexao(self):
        self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

    def receive_connection_success(self):
        messagebox.showinfo(message='Conectado ao servidor') 
        self.send_match(2)

    def send_match(self, amount_of_players):	# Pyng use case "send match"
        self.server_proxy.send_match(amount_of_players)
        
    def receive_match(self, partida):
        messagebox.showinfo(message='Partida iniciada') 
        print('********** ORDEM: ', partida.position)
        print('********** match_id: ', partida.match_id)
        self.set_partida_id(partida.match_id)
        if (partida.position == 1):
            self.habilitar_interface()
        self.meuTabuleiro.start_partida(self.get_local_habilitado())
        novo_estado = self.meuTabuleiro.get_estado()
        self.atualizar_interface_usuario(novo_estado)

