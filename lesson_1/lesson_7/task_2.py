from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, size):
        self.size = int(size)

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5)


class Suit(Cloth):

    @property
    def consumption(self):
        return round(self.size * 2 + 0.3)


coat = Coat(10)
print(coat.consumption)
suit = Suit(30)
print(suit.consumption)
