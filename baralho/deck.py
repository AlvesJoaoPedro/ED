from .naipes import Paus, Copas, Ouros, Espadas
from random import shuffle
import os

class Baralho:
    def __init__(self) -> list:
        self.paus = Paus()
        self.copas = Copas()
        self.ouros = Ouros()
        self.espadas = Espadas()
        self.__Baralho = self.paus.GetDeck() + self.copas.GetDeck() + self.ouros.GetDeck() + self.espadas.GetDeck()

    def MostrarBaralho(self):
        stringBaralho = ", ".join(str(item) for item in self.__Baralho)
        print(stringBaralho)

    def _Embaralhar(self):
        shuffle(self.__Baralho)
        print("Embaralhando...")
        input("Pressione qualquer tecla para continuar: ")
        os.system('cls')
        self.MostrarBaralho()

    def GetBaralho(self):
        return self.__Baralho