'''
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».

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


class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        '''возвращает true для всех десертов'''

        if self.flavor == 'black licorice':
            return False

        return True


# Тесты
a = JellyBean('name', 100, 'black licoric')
a.is_delicious()
