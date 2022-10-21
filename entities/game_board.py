from ast import Try
from typing import Tuple
from .player import Player
from .property import Property
import random

"""Classe cria e inicializa um tabuleiro."""

class GameBoard:

    QT_PROPERTIES = 20

    def __init__(self) -> None:
        self.properties = self.start_game_board()

    def start_game_board(self):
        """Inicia o tabuleiro, carregando imóveis e definindo seus valores aleatóriamente."""
        properties = []
        for i in range(0, self.QT_PROPERTIES):
            properties.append(Property(sale_value=round(random.uniform(100.00, 300.00), 2), 
                                        rent_value=round(random.uniform(30.00, 90.00), 2)))
        return properties

    def random(value_init: float, value_end: float):
        """Retorna valores aleatórios dentro de um range."""
        return round(random.uniform(value_init, value_end), 2)

    def move_player(self, player: Player, property: int):
        """Move o jogador pelo tabuleiro e acompanha os registros de compra de imóvel."""
        self.properties[player.position_property].remove_position_player(player)
        player.position_property = property
        self.properties[property].position_player(player)
        bool_buy = False
        balance_value = 0
        if self.properties[property].owner == None:
            bool_buy, balance_value = player.buy_or_rent(self.properties[property].sale_value, 
                       self.properties[property].rent_value, self.properties[property].owner)
            if bool_buy:
                self.properties[property].owner = player
        return (bool_buy, balance_value)

    def get_position_property(self, dice_value: int, player: Player):
        """Retorna a posição que o jogador vai estar no tabuleiro, a propriedade."""
        full_turn = False
        try:
            idx = self.properties.index(player)
            print('conseguiu - > ', idx)
            if idx + dice_value < self.QT_PROPERTIES:
                idx = idx + dice_value
            else:
                idx = (idx + dice_value) - self.QT_PROPERTIES
                full_turn = True
        except:
            idx = dice_value
        return (idx, full_turn)


