from datetime import date

from dateutil import easter
from dateutil.parser import parse

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(f'{date.today():%d.%m.%Y}')
    get_employees()
    calculate_salary()

    year = int(input('\nУкажите год для определения даты Пасхи: '))
    print(f'{easter.easter(year, method=2):%d.%m.%Y}\n')

    print('Пример парсинга дат из файлов журнала и т.п.')
    logline = 'INFO 2023-01-01T00:00:01 Happy new year, human.'
    print(f'На входе имеется строка: {logline}')
    timestamp = parse(logline, fuzzy=True)
    print(f'Результат парсинга: {timestamp}')
