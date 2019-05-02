# -*- coding: utf-8 -*-
from mao import Mao

class BlackJack(object):

	def __init__(self, baralho):
		self.fichas = 100
		self.baralho = baralho
		self.naipes = baralho.getNaipes()

	# Mostra o título do jogo no CLI
	def mostra_titulo(self):
		print("{} {} Bem vindo(a)s ao Jogo de BlackJack {} {}"
			.format(
				self.naipes[0]['simbolo'], 
				self.naipes[1]['simbolo'],
				self.naipes[2]['simbolo'], 
				self.naipes[3]['simbolo']))

	# Inicia o jogo
	def init(self):
		self.distribuiCartas()
		
	def fazAposta(self):
		aposta = 0
		print("Quantas fichas gostaria de apostar?")
		while aposta == 0:
			aposta = int(input())
			if aposta > 0:
				self.fichas -= aposta
				break
			else:
				print("O número de fichas da aposta deve ser válido!")
		print("Você possui {} fichas para apostar além das {} apostadas".format(
			str(self.fichas), 
			aposta))

	def distribuiCartas(self):

		self.baralho.embaralhaCartas()

		mao_jogador = Mao()
		mao_dealer = Mao()

		# Duas cartas para o Jogador
		mao_jogador.addCarta(baralho.pegaCarta())
		mao_jogador.addCarta(baralho.pegaCarta())

		# Duas cartas para o Dealer
		mao_dealer.addCarta(baralho.pegaCarta())
		mao_dealer.addCarta(baralho.pegaCarta())
