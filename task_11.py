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
        if type(self.calories) not in (int, float):
            return False

        if not self.calories < 200:
            return False

        return True

    def is_delicious(self):
        '''возвращает true для всех десертов'''

        if not self.__class__ == Dessert:
            return False

        return True


# Test commands:
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
# test_name

dessert.name = "test_name2"
print(dessert.name)
# test_name2

if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
# test_calories

dessert.calories = "test_calories2"
print(dessert.calories)
# test_calories2

if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
# True

if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.is_healthy())
