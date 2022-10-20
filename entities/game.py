from entities.game_board import GameBoard
from game_board import GameBoard
from type_players import IMPULSIVE, RIGOROUS, PRUDENT, RANDOM
from player import Player
import random

"""Classe cria uma partida do jogo, instanciando seus componentes."""

class Game:

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
        player = None
        players = [self.player_impulsive, self.player_rigorous, self.player_prudent, self.player_random]
        for i in range(0, 4):
            player = random.choice(players)
            ord.append(player)
            players.pop(player)
        count = 0
        while count < 1000:
            players[0].play(self.dice_roller())


