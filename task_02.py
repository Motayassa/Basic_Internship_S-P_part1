'''Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.'''


def coincidence(*args):
    '''Возвращает список элементов из массива list, значения которого входят в
    указанный диапазон range

    '''
    if len(args) < 2:
        return []

    list, range = args

    if not isinstance(list, type(list)) or not isinstance(range, type(range)):
        return []

    list_result = [x for x in list if x in range]

    return list_result


# Тесты
a = coincidence([1, 2, 3, 4, 5], range(3, 6))  # => [3, 4, 5]
b = coincidence()  # => []
c = coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))  # => [1, 2, 2.5]
print(a, b, c, sep='\n')
