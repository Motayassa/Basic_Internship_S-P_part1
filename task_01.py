'''Разработайте метод is_palindrome(string), который будет определять,
является ли параметр string палиндромом (строкой, которая читается
одинаково как сначала так и с конца), при условии игнорирования пробелов,
знаков препинания и регистра.

'''


from string import punctuation


def is_palindrome(string):
    '''Определяет является ли параметр палиндромом,
    без учета знаков препинания, пробелов и регистра

    '''
    new_string = str(string)  # создаем копию строки, чтобы метод ее не изменял

    new_string = [x for x in new_string if x not in punctuation + ' ']
    new_string = ''.join(new_string).lower()
    if new_string == new_string[::-1]:
        return True
    return False


#  Tests
a = is_palindrome("A man, a plan, a canal -- Panama")  # => True
b = is_palindrome("Madam, I'm Adam!")  # => True
c = is_palindrome(333)  # => True
d = is_palindrome(None)  # => False
e = is_palindrome("Abracadabra")  # => False'''

print(a, b, c, d, e, sep='\n')
