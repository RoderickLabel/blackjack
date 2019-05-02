# -*- coding: utf-8 -*-
class Carta:

	def __init__(self, carta, valor, naipe, simbolo):
		self.carta = carta
		self.valor = valor
		self.naipe = naipe
		self.simbolo = simbolo

	def getCarta(self):
		return self.carta

	def getValor(self):
		return self.valor

	def getNaipe(self):
		return self.naipe

	def getSimbolo(self):
		return self.simbolo

