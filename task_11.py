'''
Реализуйте класс Dessert c геттерами и сеттерами name и calories,
конструктором, принимающим на вход name и calories
(не обязательные параметры), а также двумя методами is_healthy
(возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).

'''


class Dessert:
    '''
    Описывает дессерты свойствами - имя и калорийность, содержит два метода.

    '''
    def __init__(self, name=None, calories=0):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_dessert):
        self._name = name_dessert
