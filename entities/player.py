import random
from .type_players import IMPULSIVE, RIGOROUS, PRUDENT, RANDOM

"""Classe define propriedades e comportamento de jogador."""
class Player:

    def __init__(self, balance_value, type_player) -> None:
        self.balance_value = balance_value
        self.type_player = type_player
        self.properties = []
        self.position_property = 0

    def buy_or_rent(self, value_sell: float, value_rent: float, owner: bool):
        """Realiza compra em função de seu comportamento ou paga aluguel."""
        if not owner:
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
                self.balance_value = self.balance_value - value_rent
                return False, self.balance_value
        else:
            self.balance_value = self.balance_value - value_rent
            return False, self.balance_value
