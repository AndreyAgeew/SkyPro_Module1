from random import choice
from typing import List


def is_start() -> None:
    """Функция проверяет нажатия Enter (без ввода значений)"""
    print('Сегодня мы потренируемся расшифровать морзянку.')
    while True:
        if input('Нажмите Enter и начнем') == '':
            break


def get_random_words(words: tuple[str]) -> str:
    """
    Передает кортеж слов для морзянки в случайном порядке
    :param: words: список слов
    :type: tuple[str]
    empty_list (List[str]) - пустой список, куда добавляются слова для морзянки в случайном порядке
    :return: список слов в случайном порядке преобразованный в кортеж
    """
    empty_list = []
    while len(empty_list) != len(words):
        rand_word = choice(words)
        if rand_word not in empty_list:
            empty_list.append(rand_word)
    return tuple(empty_list)


def game_encryption_morse(words: tuple[str], morse_dict: dict[str, str], answers: List[bool]) -> None:
    """
    Функция шифрует слово в морзе, и пользователь отгадывает его
    так же передает верные и неверные ответы
    :param words: список слов
    :type: tuple[str]
    :param morse_dict: словарь морзе
    :type: dict[str, str]
    :param answers: список статистики отгаданных и не отгаданных слов
    :type: List[bool]
    """
    for i_word in range(len(words)):
        print(f'Слово {i_word + 1}', end=' ')
        for letter in words[i_word]:
            print(morse_dict[letter], end="")
        if words[i_word].lower() != str(input('\n\n')).lower():
            print(f'Неверно, {words[i_word]}')
            answers.append(False)
        else:
            print(f'Верно, {words[i_word]}')
            answers.append(True)


def output_statistics(answers: List[bool]) -> None:
    """Функция выводит статистику игры"""
    print(f'\nВсего задачек: {len(answers)}\n'
          f'Отвечено верно: {answers.count(True)}\n'
          f'Отвечено неверно: {answers.count(False)}')
