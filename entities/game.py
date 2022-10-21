from .game_board import GameBoard
from .type_players import IMPULSIVE, RIGOROUS, PRUDENT, RANDOM
from .player import Player
import random

"""Classe cria uma partida do jogo, instanciando seus componentes."""

class Game:

    TIME_OUT = 1000

    def __init__(self) -> None:
        self.game_board = GameBoard()
        self.player_impulsive = Player(300.00, IMPULSIVE)
        self.player_rigorous = Player(300.00, RIGOROUS)
        self.player_prudent = Player(300.00, PRUDENT)
        self.player_random = Player(300.00, RANDOM)

    def dice_roller(self):
        """Jogar o dado."""
        return random.randrange(1, 7)

    def start_game(self):
        """Inicia o jogo."""
        ord = []
        temp_player = None
        players = [self.player_impulsive, self.player_rigorous, self.player_prudent, self.player_random]
        for i in range(0, 4):
            temp_player = random.choice(players)
            ord.append(temp_player)
            players.remove(temp_player)
        count = 0
        while count < self.TIME_OUT and len(ord) > 1:
            for player in ord:
                idx, full_turn = self.game_board.get_position_property(self.dice_roller(), player)
                if full_turn:
                    player.balance_value += 100
                _, balance_value = self.game_board.move_player(player, idx)
                if balance_value < 0:
                    ord.remove(player)
            count += 1
        if len(ord) == 1:
            return {'time_out': False, 'turn': count, 'win': player}
        elif count == self.TIME_OUT:
            return {'time_out': True, 'turn': count, 'win': None}
            


