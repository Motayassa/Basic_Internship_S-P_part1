'''
Разработать методы для программы Камень-Ножницы-Бумага.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы,
R - камень, и функционировать следующим образом:

• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от 'R', 'P' или 'S' необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.

'''


class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(game):
    '''
    Метод для игры Камень-Ножницы-Бумага. Возвращает имя и ход победителя,
    доступное количество игроков - 2. При одинаковой стратегии
    выигрывает игрок №1. P - бумага, S - ножницы, R - камень

    '''

    if not len(game) == 2:
        raise WrongNumberOfPlayersError('Неверное кол-во игроков, доступно 2')

    gamer1, gamer2 = game  # распаковка первоначальной структуры
    if gamer1[1] not in ('R', 'P', 'S') or gamer2[1] not in ('R', 'P', 'S'):
        raise NoSuchStrategyError('В игре участвуют только камень - R, ножницы - S и бумага - P')


# Тесты
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])  # => WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']])  # => NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']])  # => 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']])  # => 'player1 P
