from random import random
from property import Property
from type_players import IMPULSIVE, RIGOROUS, PRUDENT, RANDOM

"""Classe define propriedades e comportamento de jogador."""
class Player:

    def __init__(self, balance_value, type_player) -> None:
        self.balance_value = balance_value
        self.type_player = type_player
        self.properties = []
        self.position_property = 0

    def buy(self, value_sell, value_rent):
        """Realiza compra em função de seu comportamento."""
        if self.type_player == IMPULSIVE:
            self.balance_value = self.balance_value - value_sell
            return True, self.balance_value
        elif self.type_player == RIGOROUS and value_rent > 50.00:
            self.balance_value = self.balance_value - value_sell
            return True, self.balance_value
        elif self.type_player == PRUDENT and value_sell <= (self.balance_value - 80.00):
            self.balance_value = self.balance_value - value_sell
            return True, self.balance_value
        elif self.type_player == RANDOM and random.choice([True, False]):
            self.balance_value = self.balance_value - value_sell
            return True, self.balance_value
        else:
            return False, self.balance_value


    def rent():
        """Realiza a jogada em função de seu comportamento."""
        pass

