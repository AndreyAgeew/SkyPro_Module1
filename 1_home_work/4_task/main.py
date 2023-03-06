def accumulation() -> float:
    """
    Функция подсчитывает и передает накопления за 12 месяцев
    total_money (float) - передается накопление за 12 месяцев
    :return: total_money
    """
    total_money: float = 0
    for _ in range(12):
        total_money += float(input('Введите сумму накопленную в этом месяце: '))
    return total_money


def output_money(total_money: float) -> None:
    """Функция выводит накопления за 12 месяцев"""
    print(f'Накопленная сумма денег за 12 месяц: {total_money}')


def main() -> None:
    """
    total_money (float) - передается накопление за 12 месяцев
    output_money (func) -  выводит накопления за 12 месяцев
    """
    total_money: float = accumulation()
    output_money(total_money)


if __name__ == '__main__':
    main()
