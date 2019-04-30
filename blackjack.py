# -*- coding: utf-8 -*-
class BlackJack(object):
	
	# irá comportar o baralho francês completo de 52 cartas
	baralho = []

	# irá conter os naipes do baralho
	naipes = []

	# armazena as cartas que estão na mesa
	mesa = {}

	# armazena as cartas que estão na mão do jogador
	maoJogador = {}

	# armazena as cartas que estão na mão do dealer
	maoDealer = {}

	def __init__(self, baralho):
		self.baralho = baralho.getBaralho()
		self.naipes = baralho.getNaipes()

	# Mostra o título do jogo no CLI
	def mostra_titulo(self):
		print("{} {} Bem vindo(a)s ao Jogo de BlackJack {} {}"
			.format(self.naipes[0]['simbolo'], self.naipes[1]['simbolo'], self.naipes[2]['simbolo'], self.naipes[3]['simbolo']))

	# Inicia o jogo
	def init(self):
		print("Jogo começando...")