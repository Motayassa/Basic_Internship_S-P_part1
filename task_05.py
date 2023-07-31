'''
Разработать метод date_in_future(integer), который вернет дату через
integer дней. Если integer не является целым числом,
то метод должен вывести текущую дату. Формат возвращаемой методом даты
должен иметь следующий вид '01-01-2001 22:33:44'.

'''


import datetime
from datetime import timedelta


def date_in_future(integer):
    '''
    Возвращает дату через integer дней, если integer является
    целым числом, иначе возвращает текущую дату

    '''

    dt = datetime.datetime.now()

    # Возвращение текущей даты
    if type(integer) is not int:
        return dt.strftime('%d-%m-%Y %H:%M:%S')

    # Возвращение даты через integer дней
    if type(integer) is int:
        days = timedelta(integer)  # число дней для прибавления к дате
        new_data = dt + days
        return new_data.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future('integer'))
print(date_in_future(2))
