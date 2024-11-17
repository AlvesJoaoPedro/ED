from player import jogador
from baralho import deck
from random import sample

class Batalha:
    def __init__(self, baralho, jogador1, jogador2):
        self.Baralho = baralho
        self.__Jogador1 = jogador1
        self.__Jogador2 = jogador2
        self.Batalhar()

    def Batalhar(self):
        baralhoAtual = self.Baralho.GetBaralho()

        # Distribuindo as cartas para os jogadores
        deckJogador1 = sample(baralhoAtual, k=13)  # Garantindo que as cartas sejam distintas
        self.__Jogador1.GetDeck().extend(deckJogador1)
        for carta in deckJogador1:
            if carta in self.Baralho.GetBaralho():
                self.Baralho.GetBaralho().remove(carta)

        deckJogador2 = sample(baralhoAtual, k=13)  # Garantindo que as cartas sejam distintas
        self.__Jogador2.GetDeck().extend(deckJogador2)
        for carta in deckJogador2:
            if carta in self.Baralho.GetBaralho():
                self.Baralho.GetBaralho().remove(carta)

        print(f"{self.__Jogador1.GetNome()} - {self.__Jogador1.GetDeck()}")
        print(f"{self.__Jogador2.GetNome()} - {self.__Jogador2.GetDeck()}")

        # Enquanto ambos os jogadores tiverem cartas, a batalha continua
        while len(self.__Jogador1.GetDeck()) > 0 and len(self.__Jogador2.GetDeck()) > 0:
            numRodadas = min(len(self.__Jogador1.GetDeck()), len(self.__Jogador2.GetDeck()))

            for x in range(numRodadas):
                # Verificando se algum jogador já ficou sem cartas
                if len(self.__Jogador1.GetDeck()) == 0:
                    print(f"{self.__Jogador1.GetNome()} ficou sem cartas!")
                    break  # Sai do loop for
                if len(self.__Jogador2.GetDeck()) == 0:
                    print(f"{self.__Jogador2.GetNome()} ficou sem cartas!")
                    break  # Sai do loop for

                cartaJogador1 = self.__Jogador1.GetDeck()[x]
                cartaJogador2 = self.__Jogador2.GetDeck()[x]

                print(f"Carta {self.__Jogador1.GetNome()}: {cartaJogador1} x {self.__Jogador2.GetNome()}: {cartaJogador2}")

                if cartaJogador1 > cartaJogador2:
                    print(f"{self.__Jogador1.GetNome()} venceu a rodada!")
                    self.__Jogador1.GetDeck().append(cartaJogador2)
                    self.__Jogador2.GetDeck().remove(cartaJogador2)
                elif cartaJogador2 > cartaJogador1:
                    print(f"{self.__Jogador2.GetNome()} venceu a rodada!")
                    self.__Jogador2.GetDeck().append(cartaJogador1)
                    self.__Jogador1.GetDeck().remove(cartaJogador1)
                else:
                    print("Rodada empatada.")

            # Verificando novamente se algum jogador ficou sem cartas após o loop for
            if len(self.__Jogador1.GetDeck()) == 0:
                print(f"{self.__Jogador1.GetNome()} ficou sem cartas!")
                break  # Sai do loop while
            if len(self.__Jogador2.GetDeck()) == 0:
                print(f"{self.__Jogador2.GetNome()} ficou sem cartas!")
                break  # Sai do loop whil
