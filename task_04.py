'''
Дан список целых чисел. Необходимо разработать метод sort_list(list),который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него.
Тесты для примеров и проверки:

'''


def sort_list(list):
    '''
    Меняет местами все минимальные и максимальные элементы list и
    добавляет в конец массива одно минимальное значение из него

    '''
    if list == []:
        return []

    min_list = min(list)
    max_list = max(list)

    for i, j in enumerate(list):
        if j == min_list:
            list[i] = max_list
        if j == max_list:
            list[i] = min_list

    list.append(min_list)

    return list


a = sort_list([])  # => []
b = sort_list([2, 4, 6, 8])  # => [8, 4, 6, 2, 2]
c = sort_list([1])  # => [1, 1]
d = sort_list([1, 2, 1, 3])  # => [3, 2, 3, 1, 1]

print(a, b, c, d, sep='\n')
