'''Разработайте метод is_palindrome(string), который будет определять,
является ли параметр string палиндромом (строкой, которая читается
одинаково как сначала так и с конца), при условии игнорирования пробелов,
знаков препинания и регистра.'''
from string import punctuation


def is_palindrome(string):
    '''Определяет является ли параметр палиндромом,
    без учета знаков препинания, пробелов и регистра'''
    if type(string) != str:
        string = str(string)
    string = [str(x) for x in string if x not in punctuation + ' ']
    string = ''.join(string).lower()
    if string == string[::-1]:
        return True
    return False
