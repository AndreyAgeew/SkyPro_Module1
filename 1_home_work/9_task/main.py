def get_amount_pythons() -> int:
    """Функция запрашивает и передает кол-во питонов"""
    return int(input('Введите кол-во питонов: '))


def output_pythons(amount_pythons: int) -> None:
    """Функция выводит кол-во питонов с правильным окончанием"""
    if amount_pythons == 1 or (amount_pythons > 20 and amount_pythons % 10 == 1) \
            and amount_pythons % 100 != 11:
        print(amount_pythons, 'питон')
    elif (amount_pythons > 1 and amount_pythons < 5) or \
            (amount_pythons > 20 and amount_pythons % 10 > 1 and amount_pythons % 10 < 5):
        print(amount_pythons, 'питона')
    elif amount_pythons == 0 or (amount_pythons > 1 and amount_pythons < 20) \
            or amount_pythons % 10 == 0 or amount_pythons % 100 >= 11 \
            or amount_pythons % 10 >= 5 or amount_pythons % 100 >= 10:
        print(amount_pythons, 'питонов')


def main() -> None:
    """
    Основная функция
    amount_pythons (int) -  передается кол-во "питонов"
        Functions:
            get_amount_pythons - запрашивает и передает кол-во "питонов"
            output_pythons - выводи кол-во "питонов" с правильным окончанием
    """
    amount_pythons: int = get_amount_pythons()
    output_pythons(amount_pythons)


if __name__ == '__main__':
    main()
