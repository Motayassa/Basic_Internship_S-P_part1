'''
Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.

'''


def combine_anagrams(words_array):
    '''Принимает на вход массив слов и разбивает их в группы по анаграммам,
    регистр букв не имеет значения при определении анаграмм.

    '''

    # Приведение слов в единый регистр
    for word in words_array:
        word.lower()

    anagram_groups = []  # хранилище для групп анаграмм

    for j in words_array:

        # отфильтровываем анаграммы в список anagrams
        anagrams = list(filter(lambda x: set(j) == set(x), words_array))

        # сохраняем анаграммы в результирущий список
        if anagrams not in anagram_groups:
            anagram_groups.append(anagrams)

    return anagram_groups


# Тест для примеров и проверки:
a = combine_anagrams(["cars", "for", "potatoes", "racs", "four",
                      "scar", "creams", "scream"])

print(a)

# [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"],
# ["creams", "scream"] ]
