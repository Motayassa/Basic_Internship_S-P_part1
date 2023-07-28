'''
Разработать методы для программы Камень-Ножницы-Бумага.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
функционировать следующим образом:

• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от 'R', 'P' или 'S' необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.

'''


'''
Тесты для примеров и проверки:
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
=> WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
=> NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
=> 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) #
=> 'player1 P
'''
