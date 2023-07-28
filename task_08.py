'''
Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs.

'''


def multiply_numbers(inputs=None):
    '''
    Возвращает произведение цифр, входящих в inputs

    '''

    if inputs is None:
        return None

    if type(inputs) == list:
        inputs = [str(x) for x in inputs]

    if type(inputs) in (int, float):
        inputs = str(inputs)

    # Список, хранящий цифры из input
    lst_number = list(map(int, filter(lambda x: x.isdigit(), inputs)))

    # проверка на случай отсутствия цифр в input
    if lst_number == []:
        return None

    # перемножение цифр из input
    multiple = 1
    for i in lst_number:
        multiple *= i

    return multiple

# Тест для примеров и проверки:
print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
