def output_washing_mode() -> None:
    """Функция выводит все режимы стиральной машины"""
    print(f'Обычный цикл стирки занимает 90 минут.\n'
          f'Экспресс-стирка длится 20 минут.\n'
          f'Стирка хлопка длится 120 минут.\n\n'
          f'Отключенный отжим сэкономит 10 минут.\n'
          f'Дополнительное полоскание добавит 10 минут.\n\n')


def get_washing_mode() -> int:
    """
    Функция подсчитывает сколько времени займет стирка и передает это время
    time_washing (int) - передается время стирки
    washing_mode (int) - передается режим стирки
    spin (str) - передается отжим вкл или выкл
    rinse (str) - передается доп. полоскание вкл или выкл
    :return: time_washing
    """
    time_washing: int = 0
    while True:
        washing_mode: int = int(input('Для обычной стирки нажмите (0)\n'
                                      'Для экспресс-стирки нажмите (1)\n'
                                      'Для стирки хлопка нажмите (2)\n'))
        if washing_mode == 0:
            time_washing += 90
            break
        elif washing_mode == 1:
            time_washing += 20
            break
        elif washing_mode == 2:
            time_washing += 120
            break
        else:
            print('Режим стирки не выбран!')
    while True:
        spin: str = str(input("Режим отжима: вкл - введите yes, отключить - no: "))
        if spin == 'yes':
            time_washing += 10
            break
        elif spin == 'no':
            break
        else:
            print('Режим отжима не выбран!')
    while True:
        rinse: str = str(input("Режим полоскания: вкл - введите yes, отключить - no: "))
        if rinse == 'yes':
            time_washing += 10
            break
        elif rinse == 'no':
            break
        else:
            print('Режим полоскания не выбран!')
    return time_washing


def output_washing_time(washing_time: int) -> None:
    """Функция выводит время стирки"""
    print(f'Стирка займет: {washing_time} минут')


def main() -> None:
    """
    Основная функция
    output_washing_mode (func) - выводит все режимы стиральной машины
    washing_time (int) - передается кол-во времени для стирки
    get_washing_mode (func) - подсчитывает и передает кол-во времени для стирки
    output_washing_time (func) - выводит кол-во времени для стирки
    """
    output_washing_mode()
    washing_time: int = get_washing_mode()
    output_washing_time(washing_time)


if __name__ == '__main__':
    main()
