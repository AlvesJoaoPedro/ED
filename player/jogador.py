class Jogador:
    def __init__(self, nome:str) -> str :
        self.__Nome = nome
        self.__Deck = []

    def GetNome(self):
        return self.__Nome

    def GetDeck(self):
        return self.__Deck