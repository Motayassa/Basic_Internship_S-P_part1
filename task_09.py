'''
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:
• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным)
• ключи со значениями меньше 10 не должны попасть в финальный
словарь
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.

'''


def connect_dicts(dict1, dict2):
    '''
    возвращает словарь, объединенный из двух переданных слоарей,
    по особым правилам

    '''

    sum_dict1 = sum(dict1.values())
    sum_dict2 = sum(dict2.values())

    if sum_dict2 >= sum_dict1:
        priority_dict = dict2
        unpriority_dict = dict1
    else:
        priority_dict = dict1
        unpriority_dict = dict2

    res_priority = {k: v for k, v in priority_dict.items() if v >= 10}

    res_unpriority = {k: v for k, v in unpriority_dict.items()
                      if k not in res_priority if
                      v >= 10}

    # создание результирующего словаря
    final_res = res_priority | res_unpriority

    # сортировка словаря по значениям
    return dict(sorted(final_res.items(), key=lambda item: item[1]))


# Тесты для примеров и проверки:
a = connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
# => { "c": 11, "b": 12 }
b = connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
# => { d: 11, "c": 12, "a": 13 }
c = connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
# => { "c": 11, "b": 12, "a": 15 }

print(a, b, c, sep='\n')
