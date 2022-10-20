from player import Player
from property import Property
import random

"""Classe cria e inicializa um tabuleiro."""

class GameBoard:

    def __init__(self) -> None:
        self.properties = self.start_game_board()

    def start_game_board(self):
        """Inicia o tabuleiro, carregando imóveis e definindo seus valores aleatóriamente."""
        properties = []
        for i in range(0, 20):
            properties.append(Property(sale_value=self.random(100.00, 300.00), 
                                        rent_value=self.random(30.00, 90.00)))
        return properties

    def random(value_init: float, value_end: float):
        """Retorna valores aleatórios dentro de um range."""
        return round(random.uniform(value_init, value_end), 2)

    def move(self, player: Player, property: int):
        self.properties[property].remove_position_player(player)
        player.position_property = property
        self.properties[property].position_player(player)
        if self.properties[property].owner == None:
            player.buy(self.properties[property].sale_value, self.properties[property].rent_value)
            self.properties[property].owner = player