#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tabuleiro import Tabuleiro
from typing import List

class BoardImage(object):
	def get_message(self) -> str:
		pass

	def set_message(self):
		pass

	def get_value(self, aLinha : int, aColuna : int) -> int:
		pass

	def set_value(self, aLinha : int, aColuna : int, aZ : int, aValue : int):
		pass

	def get_status_partida(self) -> int:
		pass

	def set_status_partida(self, aStatus_partida : int):
		pass

	def __init__(self):
		self._message : str = None
		self.__array_5__5____map : int = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None

