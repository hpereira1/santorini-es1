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

        self.mainJanela.resizable(False, False)
        self.mainJanela.geometry("800x600")
        
        self.mainFrame = Frame(self.mainJanela, padx=44, pady=40, bg="gray")
        self.messageFrame = Frame(self.mainJanela, padx=4, pady=4, bg="gray")


        self.grass_image1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png'))
        self.grass_image2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama2.png'))
        
        self.boardView = []
        for i in range(5):
            self.mainFrame.grid_rowconfigure(i, weight=1)
            row = []
            for j in range(5):
                self.mainFrame.grid_columnconfigure(j, weight=1)
                grass_image = self.grass_image1 if (i + j) % 2 == 0 else self.grass_image2
                label = Label(self.mainFrame, image=grass_image)
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
        self.desabilitar_interface()
        self.set_partida_id('')

        self.add_listener()	# Pyng use case "add listener"
        self.enviar_conexao()	# Pyng use case "send connect"

        self.mainJanela.mainloop()
        
    @staticmethod
    def resize_image(image_path, width, height):
        image = Image.open(image_path)  # Abra a imagem usando o PIL
        image = image.resize((width, height), Image.LANCZOS)  # Redimensione a imagem
        return ImageTk.PhotoImage(image)
    
    def click(self, event, linha, coluna):
        pass  # Implementação específica vai aqui

    def atualizar_interface_usuario(self, novo_estado):
        pass  # Implementação específica vai aqui

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
        pass  # Implementação específica vai aqui

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

