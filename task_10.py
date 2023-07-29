'''
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов.
Тесты для примеров и проверки:

'''


def count_words(string):
    '''
    Возвращает словарь со статистикой частоты употребления входящих слов
    во входной строке.

    '''

    from string import punctuation
    # Копируем входную строку, чтобы не менять входные данные
    string = string[:].lower()
    # Приводим строку к формату без знаков препинания
    string = (''.join(char for char in string if char not in punctuation))

    res_dict = {}  # результирующий пустой словарь

    # формирование словаря со статистикой частоты употребления слов
    for word in string.split():
        if word not in res_dict:
            res_dict[word] = 1
            continue
        if word in res_dict:
            res_dict[word] += 1

    return res_dict


# Тесты
print(count_words("A man, a plan, a canal -- Panama"))
# => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo"))
# => {"doo": 3, "bee": 2}
