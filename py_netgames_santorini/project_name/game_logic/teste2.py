import tkinter as tk
import random
import os
from tkinter import *
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from PIL import Image, ImageTk
from py_netgames_model.messaging.message import MatchStartedMessage, MoveMessage

class App(PyNetgamesServerListener):
    def __init__(self, root):
        self.add_listener()
        self.send_connect()
        self.root = root
        self.root.configure(bg='darkgray')
        self.button = tk.Button(root, text="Conectar", command=self.create_board, width=30, height=10, bg='lightgray')
        self.button.pack()
        self.board_size = 500  # Adicione o tamanho do tabuleiro aqui
        self.cell_size = self.board_size // 5  # O tamanho de cada célula é o tamanho do tabuleiro dividido pelo número de células

    def create_board(self):
        self.board = tk.Toplevel(self.root)
        self.board.geometry("500x500")
        self.tiles = []
        self.grass_image1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama1.png'))
        self.grass_image2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'imagens/Grama2.png'))
        #self.grass_image1 = self.resize_image('imagens/Grama1.png', self.cell_size, self.cell_size)  # Adicione o caminho para sua primeira imagem aqui
        #self.grass_image2 = self.resize_image('imagens/Grama2.png', self.cell_size, self.cell_size)  # Adicione o caminho para sua segunda imagem aqui
        for i in range(5):
            self.board.grid_rowconfigure(i, weight=1)
            row = []
            for j in range(5):
                self.board.grid_columnconfigure(j, weight=1)
                grass_image = self.grass_image1 if (i + j) % 2 == 0 else self.grass_image2
                label = tk.Label(self.board, image=grass_image)
                label.image = grass_image
                label.grid(row=i, column=j, sticky='news')
                label.bind('<Button-1>', lambda event, i=i, j=j: self.on_tile_click(i, j))
                row.append(label)
            self.tiles.append(row)
        self.board.update()
        self.spawn_figures()


    @staticmethod
    def resize_image(image_path, width, height):
        image = Image.open(image_path)  # Abra a imagem usando o PIL
        image = image.resize((width, height), Image.LANCZOS)  # Redimensione a imagem
        return ImageTk.PhotoImage(image)  # Converta a imagem redimensionada para um objeto PhotoImage do tkinter

    def spawn_figures(self):
        positions = random.sample([(i,j) for i in range(5) for j in range(5)], 4)  # Agora selecionamos 4 posições
        cell_size = self.cell_size
        self.figure_images = [
            [self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog1.png'), cell_size, cell_size), 
            self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog12.png'), cell_size, cell_size)],  # Adicione os caminhos para as imagens do primeiro jogador aqui
            [self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog2.png'), cell_size, cell_size), 
            self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog22.png'), cell_size, cell_size)],   # Adicione os caminhos para as imagens do segundo jogador aqui
            [self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog1.png'), cell_size, cell_size), 
            self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog12.png'), cell_size, cell_size)],  # As imagens do terceiro jogador são as mesmas do primeiro jogador
           [self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog2.png'), cell_size, cell_size), 
            self.resize_image(os.path.join(os.path.dirname(__file__), 'imagens/jog22.png'), cell_size, cell_size)]   # As imagens do quarto jogador são as mesmas do segundo jogador
        ]
        for pos, figure_images in zip(positions, self.figure_images):
            i, j = pos
            figure_image = figure_images[0] if (i + j) % 2 == 0 else figure_images[1]
            label = self.tiles[i][j]
            label.config(image=figure_image)
            label.image = figure_image

    def on_tile_click(self, i, j):
        if self.tiles[i][j].cget('image') in [str(img) for sublist in self.figure_images for img in sublist]:
            print(f"Construtor na posição ({i}, {j}) foi selecionado")
        else:
            print(f"A célula na posição ({i}, {j}) está vazia")

    #-----------------------------------------------Pynetgames--------------------------------------------------------------

    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)

    def send_connect(self):
        self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

    def send_match(self):
        self.server_proxy.send_match(2)

    def receive_connection_success(self):
        print('****************conectado****************')
        self.send_match()

    def receive_disconnect(self):
        pass

    def receive_error(self, error: Exception):
        pass

    def receive_match(self, match: MatchStartedMessage):
        print('********** PARTIDA INICIADA **********')
        print('********** ORDEM: ', match.position)
        print('********** match_id: ', match.match_id)

    def receive_move(self, match: MoveMessage):
        pass


root = tk.Tk()
app = App(root)

root.mainloop()
