def get_today() -> int:
    """Функция запрашивает сегодняшний день и передает его"""
    return int(input('Введите, какой сегодня день: '))


def salary_day(today: int)->None:
    """Функция выводит ближайший день зарплаты"""
    if today < 11:
        print(f'Ближайшая зарплата 10 числа, через {10 - today} д.')
    elif today < 26:
        print(f'Ближайшая зарплата 25 числа, через {25 - today} д.')
    else:
        print(f'Ближайшая зарплата 10 числа, через {40 - today} д.')


def main() -> None:
    """
    Основная функция
    today (int) - передается сегодняшний день
        Functions:
            get_today - запрашивает и передает сегодняшний день
            salary_day - выводит ближайший день зарплаты и через сколько это дней
    """
    today = get_today()
    salary_day(today)


if __name__ == '__main__':
    main()
