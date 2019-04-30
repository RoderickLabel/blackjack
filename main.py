from baralhofrances import BaralhoFrances as Baralho
from blackjack import BlackJack

def main():
	baralho = Baralho()
	game = BlackJack(baralho)
	game.mostra_titulo()
	game.init()

if __name__ == '__main__':
	main()