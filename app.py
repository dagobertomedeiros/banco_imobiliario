import statistics
from entities.game import Game

class App:

    SIMULATIONS = 300

    def __init__(self) -> None:
        pass

    def run(self):
        qt_time_out = 0
        avg_turn = []
        win_players = {'IMPULSIVE': 0, 'RIGOROUS': 0, 'PRUDENT':0, 'RANDOM': 0}
        for i in range(0, self.SIMULATIONS):
            dic = Game().start_game()
            if dic['time_out'] == True:
                qt_time_out += 1
            avg_turn.append(dic['turn'])
            if dic['win'] != None:
                if dic['win'].type_player == 1:
                    win_players['IMPULSIVE'] += 1
                elif dic['win'].type_player == 2:
                    win_players['RIGOROUS'] += 1
                elif dic['win'].type_player == 3:
                    win_players['PRUDENT'] += 1
                elif dic['win'].type_player == 4:
                    win_players['RANDOM'] += 1
        print('Partidas terminam por time out (1000 rodadas): {}'.format(qt_time_out))
        print('Quantidade média de turnos por partida: {}'.format(round(statistics.mean(avg_turn), 2)))
        dic_max = {'IMPULSIVO': round((win_players['IMPULSIVE']/self.SIMULATIONS), 2),
                   'EXIGENTE': round((win_players['RIGOROUS']/self.SIMULATIONS), 2),
                   'CAUTELOSO': round((win_players['PRUDENT']/self.SIMULATIONS), 2),
                   'ALEATÓRIO': round((win_players['RANDOM']/self.SIMULATIONS), 2)}
        print('Porcentagem de vitórias por comportamento dos jogadores: \n' +
            'IMPULSIVO -> {:2.2%} \nEXIGENTE -> {:2.2%} \nCAUTELOSO -> {:2.2%} \nALEATÓRIO -> {:2.2%}'.format(
                                              dic_max['IMPULSIVO'], 
                                              dic_max['EXIGENTE'], 
                                              dic_max['CAUTELOSO'], 
                                              dic_max['ALEATÓRIO']))
        
        print('O comportamento que mais vence: {}'.format(max(dic_max, key=dic_max.get)))



if __name__ == "__main__":
    app = App()
    app.run()