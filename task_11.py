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

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        '''возвращает true при условии калорийности десерта менее 200'''

        if not self.calories < 200:
            return False

        return True

    def is_delicious(self):
        '''возвращает true для всех десертов'''

        if not self.__class__ == Dessert:
            return False

        return True


# Тесты
a = Dessert()
a = Dessert('name', 200)
print(a.name)
print(a.calories)
a.is_healthy()
a.is_delicious()
