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

    res = gamer1_vs_gamer2(gamer1, gamer2)

    return f'{res[0]} {res[1]}'


def gamer1_vs_gamer2(gamer1, gamer2):  # Вспомогательный метод
    '''
    Возращает победителя в игре камень-ножницы-бумага,
    при ничьей побеждает игрок №1

    '''
    if (
        ('R' in gamer1 and 'S' in gamer2) or
        ('S' in gamer1 and 'P' in gamer2) or
        ('P' in gamer1 and 'R' in gamer2)
    ):
        return gamer1

    if gamer1[1] == gamer2[1]:
        return gamer1

    if (
        ('R' in gamer2 and 'S' in gamer1) or
        ('S' in gamer2 and 'P' in gamer1) or
        ('P' in gamer2 and 'R' in gamer1)
    ):
        return gamer2


# Тесты
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
# => WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']])  # => NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']])  # => 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']])  # => 'player1 P
