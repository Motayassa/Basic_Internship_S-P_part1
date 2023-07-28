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

    # Список, хранящий числа из input
    lst_number = list(map(int, filter(lambda x: x.isdigit(), inputs)))


# Тест для примеров и проверки:
multiply_numbers()  # => None
multiply_numbers('ss')  # => None
multiply_numbers('1234')  # => 24
multiply_numbers('sssdd34')  # => 12
multiply_numbers(2.3)  # => 6
multiply_numbers([5, 6, 4])  # => 120
