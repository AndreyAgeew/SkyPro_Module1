from random import choice
from typing import List, Dict


def is_start() -> None:
    """Функция проверяет нажатия Enter (без ввода значений)"""
    print('Сегодня мы потренируемся расшифровать морзянку.')
    while True:
        if input('Нажмите Enter и начнем') == '':
            break


def morse_code() -> Dict:
    """Функция передает словарь зашифровки морзе"""
    return {
        " ": "/",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }


def get_words() -> List[str]:
    """Функция передает список слов для морзянки"""
    return ['snake', 'code', 'list', 'well played', 'soul', 'next']


def get_random_word(words: List[str]) -> str:
    """
    Функция передает случайное слово из списка и удаляет его из самого списка
    :param: words: список слов
    :type: List[str]
    :return: случайное слово из списка
    """
    return words.pop(words.index(choice(words)))


def game_encryption_morse(words_list: List[str], morse_dict: Dict, answers: List[bool]) -> None:
    """
    Функция шифрует слово в морзе, и пользователь отгадывает его
    так же передает верные и неверные ответы
    :param words_list: список слов
    :type: List[str]
    :param morse_dict: словарь морзе
    :type: Dict
    :param answers: список статистики отгаданных и не отгаданных слов
    :type: List[bool]
    tmp_word (str) - передается случайное слово из списка слов
    """
    for i_word in range(len(words_list)):
        tmp_word: str = get_random_word(words_list)
        print(f'Слово {i_word + 1}', end=' ')
        for letter in tmp_word:
            print(morse_dict[letter], end="")
        if tmp_word.lower() != str(input('\n\n')).lower():
            print(f'Неверно, {tmp_word}')
            answers.append(False)
        else:
            print(f'Верно, {tmp_word}')
            answers.append(True)


def output_statistics(answers: List[bool]) -> None:
    """Функция выводит статистику игры"""
    print(f'\nВсего задачек: {len(answers)}\n'
          f'Отвечено верно: {answers.count(True)}\n'
          f'Отвечено неверно: {answers.count(False)}')


def main() -> None:
    """
    words (List[str]) - передается список слов для морзянки
    morse_dict (Dict) - передается словарь морзянки
    answers (List[bool]) - передается правильные и неправильные ответы
        Functions:
            is_start - проверяет нажатие enter и вводит приветственное сообщение
            get_words - передает список слов
            morse_code - передает код(словарь) морзянки
            game_encryption_morse - шифрует слово в морзе, и пользователь отгадывает его
                                    так же передает верные и неверные ответы
            output_statistics - выводит статистику игры
    """
    is_start()
    words: List[str] = get_words()
    morse_dict: Dict = morse_code()
    answers: List[bool] = []
    game_encryption_morse(words, morse_dict, answers)
    output_statistics(answers)


if __name__ == '__main__':
    main()
