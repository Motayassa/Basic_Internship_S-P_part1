'''
Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве.

'''


def max_odd(array):
    '''Возвращает максимальный нечетный элемент из списка array'''

    odd_lst = [x for x in array if type(x) in (int, float) and x % 2 != 0]

    if odd_lst == []:
        return None

    return int(max(odd_lst))  # преобразуем вывод в integer


# Тесты для примеров и проверки:
a = max_odd([1, 2, 3, 4, 4])  # => 3
b = max_odd([21.0, 2, 3, 4, 4])  # => 21
c = max_odd(['ololo', 2, 3, 4, [1, 2], None])  # => 3
d = max_odd(['ololo', 'fufufu'])  # => None
e = max_odd([2, 2, 4])  # => None

print(a, b, c, d, e, sep='\n')
