def get_weather() -> str:
    """Функция запрашивает и передает погоду"""
    return str(input("Какая сегодня погода? "))


def is_sunny(weather: str) -> None:
    """Функция проверяет солнечная погода или нет"""
    if weather.lower() == 'солнечная':
        print('Возьми с собой очки')
    else:
        print('Возьми с собой зонт')


def output_end_work() -> None:
    """Функция выводит завершающие сообщение"""
    print('Хорошего дня!')


def main() -> None:
    """
    Основная функция
     weather (str) - передается погода
        Functions:
            get_weather - запрашивает и передает погоду
            is_sunny - проверяет солнечная погода или нет
            output_end_work - выводит завершающие сообщение
    """
    weather: str = get_weather()
    is_sunny(weather)
    output_end_work()


if __name__ == '__main__':
    main()
