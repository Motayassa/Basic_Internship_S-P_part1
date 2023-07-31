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

        if type(self.calories) not in (int, float):
            return False

        if not self.calories < 200 or type(self.calories) not in (int, float):
            return False

        return True

    def is_delicious(self):
        '''возвращает true для всех десертов'''

        if not self.__class__ == Dessert:
            return False

        return True


class JellyBean(Dessert):
    '''
    Расширяет класс Dessert, добавляя новое свойство - flavor
    Переопределяет метод is_delicious

    '''
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
        '''
        возвращает true для всех десертов, кроме десертов со свойством
        flavor = 'black licorice'
        '''

        if self.flavor == 'black licorice':
            return False

        return True


# Test commands:
dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
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
dessert.flavor = "test_flavor"
print(dessert.flavor)
# test_flavor

print(dessert.is_healthy())
