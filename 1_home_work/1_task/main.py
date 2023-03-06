def get_temperature() -> float:
    """Функция запрашивает у пользователя температуру"""
    return float(input('Введите температуру по Фаренгейту: '))


def convert_temperature(temperature: float) -> float:
    """
    Функция конвертирует температуру по Фаренгейту в Цельсии
    :param temperature: температура по Фаренгейту
    :type: float
    :return: температура по цельсию
    :rtype: float
    """
    return round((temperature - 32) * 5 / 9, 2)


def output_temperature(temperature_f: float, temperature_c: float) -> None:
    """Функция выводит преобразованную температуру"""
    print(f'{temperature_f} по Фаренгейту равна {temperature_c} по Цельсию')


def main() -> None:
    """
    Основная функция
    temperature_f (float) - передается температура по Фаренгейту
    temperature_c (float) - передается преобразованная температура в Цельсиях
        Functions:
            get_temperature -  передает температуру по Фаренгейту
            convert_temperature - конвертирует Цельсии в Фаренгейты
            output_temperature - выводит температуру
    """
    temperature_f: float = get_temperature()
    temperature_c: float = convert_temperature(temperature_f)
    output_temperature(temperature_f, temperature_c)


if __name__ == '__main__':
    main()
