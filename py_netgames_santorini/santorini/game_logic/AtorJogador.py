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
        self.ultima_celula_clicada = None

        self.mainJanela.geometry("500x550")
        self.mainJanela.resizable(False, False)
        self.mainJanela.grid_rowconfigure(0, weight=1)
        self.mainJanela.grid_columnconfigure(0, weight=1)
        
        self.mainFrame = Frame(self.mainJanela, bg="gray")
        self.mainFrame.grid(row=0, column=0, sticky="nsew", padx=44, pady=40)
        
        self.messageFrame = Frame(self.mainJanela, bg="gray")
        self.messageFrame.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        self.grass_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png')).resize((80, 80)))
        self.andar1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/Andar1.png')).resize((80, 80)))
        self.andar2 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/Andar2.png')).resize((80, 80)))
        self.andar3 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/Andar3.png')).resize((80, 80)))
        self.andar4 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/Andar4.png')).resize((80, 80)))
        self.j1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/J1g1.png')).resize((80, 80)))
        self.j2 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/J2g1.png')).resize((80, 80)))
        self.a1j2 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a1j2.png')).resize((80, 80)))
        self.a1j1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a1j1.png')).resize((80, 80)))
        self.a2j1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a2j1.png')).resize((80, 80)))
        self.a2j2 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a2j2.png')).resize((80, 80)))
        self.a3j1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a3j1.png')).resize((80, 80)))
        self.a3j2 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imagens/a3j2.png')).resize((80, 80)))
        
    

        self.boardView = []
        for i in range(5):
            self.mainFrame.grid_rowconfigure(i, weight=1)
            self.mainFrame.grid_columnconfigure(i, weight=1)

        self.boardView = []
        for i in range(5):
            row = []
            for j in range(5):
                # grass_image = self.grass_image1 if (i + j) % 2 == 0 else self.grass_image2
                label = Label(self.mainFrame, bd = 2, relief="solid", image=self.grass_image)
                # label = Label(self.mainFrame, image=self.grass_image, bd = 2, relief="solid")
                label.image = self.grass_image
                label.grid(row=i, column=j)
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
        if self.ultima_celula_clicada is not None:
            self.ultima_celula_clicada.config(bd = 2, relief = "solid")
        label_clicada = self.boardView[linha][coluna]
        label_clicada.config(bd= 4, bg = 'purple', relief = "raised")
        self.ultima_celula_clicada = label_clicada
        if (self.get_local_habilitado()):            
            jogada_a_enviar = self.meuTabuleiro.click(linha, coluna)
            novo_estado = self.meuTabuleiro.get_estado()
            self.atualizar_interface_usuario(novo_estado)
            if (bool(jogada_a_enviar)):
                self.server_proxy.send_move(self.get_partida_id(), jogada_a_enviar)
                if self.meuTabuleiro.get_jogador_desabilitado() == self.meuTabuleiro._jogadores[0]:
                    self.desabilitar_interface()
        else: 
            messagebox.showinfo(message='Você não está habilitado para jogar')



    def atualizar_interface_usuario(self, novo_estado : BoardImage):
        if not isinstance(novo_estado, BoardImage):
            raise TypeError("novo_estado deve ser uma instância de BoardImage")
        self.labelMessage['text']=novo_estado.get_message()
        for x in range(5):
            for y in range(5):
                label = self.boardView[x][y]
                dados_cel = novo_estado.get_value(x, y)
                # print(f"Célula ({x}, {y}): Nível do andar = {dados_cel[0]}, Ocupação = {dados_cel[1]}")
                if not isinstance(dados_cel, list) or len(dados_cel) != 2:
                    raise ValueError("dados_cel deve ser uma lista com dois elementos")
                if dados_cel[1]==0: # n ocupado
                    if dados_cel[0] == 0:
                        label['image'] = self.grass_image
                    elif dados_cel[0] == 1:
                        label['image'] = self.andar1
                    elif dados_cel[0] == 2:
                        label['image'] = self.andar2
                    elif dados_cel[0] == 3:
                        label['image'] = self.andar3
                    elif dados_cel[0] == 4:
                        label['image'] = self.andar4
                    
                elif dados_cel[1]==1: #ocupado jog1
                    if dados_cel[0] == 0:
                        label['image'] = self.j1
                    elif dados_cel[0] == 1:
                        label['image'] = self.a1j1
                    elif dados_cel[0] == 2:
                        label['image'] = self.a2j1
                    elif dados_cel[0] == 3:
                        label['image'] = self.a3j1
                    
                elif dados_cel[1]==2: #ocupado jog2
                    if dados_cel[0] == 0:
                        label['image'] = self.j2
                    elif dados_cel[0] == 1:
                        label['image'] = self.a1j2
                    elif dados_cel[0] == 2:
                        label['image'] = self.a2j2
                    elif dados_cel[0] == 3:
                        label['image'] = self.a3j2
    
                        
        
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
        # print(received_move)
        self.meuTabuleiro.click(int(received_move['linha']), int(received_move['coluna']))
        novo_estado = self.meuTabuleiro.get_estado()
        self.atualizar_interface_usuario(novo_estado)
        if self.meuTabuleiro.get_jogador_habilitado() == self.meuTabuleiro._jogadores[0]:
            self.habilitar_interface()

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
        self.set_partida_id(partida.match_id)
        if (partida.position == 1):
            self.habilitar_interface()
        self.meuTabuleiro.start_partida(self.get_local_habilitado())
        novo_estado = self.meuTabuleiro.get_estado()
        self.atualizar_interface_usuario(novo_estado)

