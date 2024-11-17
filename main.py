from baralho import deck
from player import jogador, crupie
from battle import batalha

deck1 = deck.Baralho()
deck1.MostrarBaralho()
"deck1.Embaralhar()"

jogador1 = jogador.Jogador("Marcos")
jogador2 = jogador.Jogador("Felipe")
jogador3 = jogador.Jogador("Vinicius")
jogador4 = crupie.Crupie("Andressa")

batalha = batalha.Batalha(deck1, jogador1, jogador2)
