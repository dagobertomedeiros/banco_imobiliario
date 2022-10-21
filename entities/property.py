"""Classe define caracteristícas de uma propriedade/imóvel no jogo."""
from .player import Player


class Property:

    def __init__(self, sale_value: float, rent_value: float) -> None:
        self.sale_value = sale_value
        self.rent_value = rent_value
        self.owner = None
        self.positioned_players = []

    def position_player(self, player: Player):
        """Define o jogador posicionado."""
        self.positioned_players.append(player)
    
    def remove_position_player(self, player: Player):
        """Define o jogador posicionado."""
        try:
            self.positioned_players.remove(player)
        except:
            pass