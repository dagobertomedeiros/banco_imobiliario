"""Classe define caracteristícas de uma propriedade/imóvel no jogo."""
from entities.player import Player


class Property:

    def __init__(self, sale_value, rent_value) -> None:
        self.sale_value = sale_value
        self.rent_value = rent_value
        self.owner = None or Player
        self.positioned_players = []

    #def property_sale(self, owner: Player):
    #    """Define dono de imóvel."""
    #    self.owner = owner
    
    def position_player(self, player: Player):
        """Define o jogador posicionado."""
        self.positioned_players.append(player)
    
    def remove_position_player(self, player: Player):
        """Define o jogador posicionado."""
        self.positioned_players.remove(player)