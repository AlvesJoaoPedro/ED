class Paus:
    def __init__(self) -> list:
        self.Valete = 11
        self.Dama = 12
        self.Rei = 13
        self.__Deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, self.Valete, self.Dama, self.Rei]

    def GetDeck(self):
        return self.__Deck

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self.__Deck)

class Ouros:
    def __init__(self) -> list:
        self.Valete = 11
        self.Dama = 12
        self.Rei = 13
        self.__Deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, self.Valete, self.Dama, self.Rei]

    def GetDeck(self):
        return self.__Deck

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self.__Deck)

class Copas:
    def __init__(self) -> list:
        self.Valete = 11
        self.Dama = 12
        self.Rei = 13
        self.__Deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, self.Valete, self.Dama, self.Rei]

    def GetDeck(self):
        return self.__Deck

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self.__Deck)

class Espadas:
    def __init__(self) -> list:
        self.Valete = 11
        self.Dama = 12
        self.Rei = 13
        self.__Deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, self.Valete, self.Dama, self.Rei]

    def GetDeck(self):
        return self.__Deck

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self.__Deck)