def get_dollars() -> float:
    """Функция запрашивает и передает кол-во долларов"""
    return float(input('Введите кол-во имеющихся долларов в банке: '))


def convert_dollars_to_rub(dollars: float) -> float:
    """Функция конвертирует доллары в рубли и передает их значение"""
    return dollars * 70.38


def convert_rub_to_euro(rub: float) -> float:
    """Функция конвертирует рубли в евро и передает их значение"""
    return rub / 100 * 1.22


def output_euro(euro: float) -> None:
    """Функция выводит кол-во евро"""
    print(f'Сейчас есть {round(euro, 2)} евро.')


def main() -> None:
    """
    dollars (float) - передается кол-во долларов
    rub (float) - передается кол-во рублей
    euro (float) - передается кол-во евро
        Functions:
            get_dollars - запрашивает и передает кол-во долларов
            convert_dollars_to_rub -  конвертирует доллары в рубли и передает их значение
            convert_rub_to_euro - конвертирует рубли в евро и передает их значение
            output_euro - выводит кол-во евро
    """
    dollars: float = get_dollars()
    rub: float = convert_dollars_to_rub(dollars)
    euro: float = convert_rub_to_euro(rub)
    output_euro(euro)


if __name__ == '__main__':
    main()