'''Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.'''


def coincidence(list=None, range=None):
    '''Возвращает список элементов из массива list, значения которого входят в
    указанный диапазон range

    '''
    if list is None or range is None:  # проверка на кол-во аргументов
        return []

    list_result = [x for x in list if type(x) in (int, float) and
                   range[0] <= x <= range[-1]]  # отбор элементов из списка

    return list_result


# Тесты
a = coincidence([1, 2, 3, 4, 5], range(3, 6))  # => [3, 4, 5]
b = coincidence()  # => []
c = coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))  # => [1, 2, 2.5]
print(a, b, c, sep='\n')
