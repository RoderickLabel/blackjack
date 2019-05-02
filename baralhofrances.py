# -*- coding: utf-8 -*-
import random
from carta import Carta

class BaralhoFrances(object):

	naipes = [
		{"nome": "paus", "simbolo": "♣"}, 
		{"nome": "ouros", "simbolo": "♦"}, 
		{"nome": "copas", "simbolo": "♥"}, 
		{"nome": "espadas", "simbolo": "♠"}
	]

	''' 
	armazena o baralho básico, sem naipes, 
	mas que servirá de modelo para compor o baralho completo
	'''
	baralhoModelo = [
		{"carta": "A", "valor": 1}, 
		{"carta": "2", "valor": 2}, 
		{"carta": "3", "valor": 3}, 
		{"carta": "4", "valor": 4}, 
		{"carta": "5", "valor": 5}, 
		{"carta": "6", "valor": 6}, 
		{"carta": "7", "valor": 7}, 
		{"carta": "8", "valor": 8}, 
		{"carta": "9", "valor": 9}, 
		{"carta": "10", "valor": 10}, 
		{"carta": "J", "valor": 10}, 
		{"carta": "Q", "valor": 10}, 
		{"carta": "K", "valor": 10}
	]

	# irá comportar o baralho francês completo de 52 cartas
	baralho = []

	# inicia o objeto 
	def __init__(self):
		self.criaBaralho()

	# Gera o Baralho Francês de 52 cartas virtualmente, trata-se de uma lista de dicionarios para cada carta
	def criaBaralho(self):
		for naipe in self.naipes:
			for carta in self.baralhoModelo:
				self.baralho.append(
					Carta(carta["carta"], carta["valor"], naipe["nome"], naipe["simbolo"]))				

	# Embaralha as cartas
	def embaralhaCartas(self):
		random.shuffle(self.baralho)

	def getBaralho(self):
		return self.baralho

	def getNaipes(self):
		return self.naipes

	def pegaCarta(self):
		return baralho.pop()