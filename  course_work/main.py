from typing import List
from config import MORSE_CODE, words_for_morse
from utils import is_start,  game_encryption_morse, output_statistics, get_random_words


def main() -> None:
    """
    words (tuple[str]) - передается кортеж слов для морзянки
    morse_dict (Dict[str,str]) - передается словарь морзянки
    answers (List[bool]) - передается правильные и неправильные ответы
        Functions:
            get_random_words -  передает кортеж слов для морзянки в случайном порядке
            is_start - проверяет нажатие enter и вводит приветственное сообщение
            game_encryption_morse - шифрует слово в морзе, и пользователь отгадывает его
                                    так же передает верные и неверные ответы
            output_statistics - выводит статистику игры
    """
    is_start()
    words: tuple[str] = get_random_words(words_for_morse)
    morse_dict: dict[str, str] = MORSE_CODE
    answers: List[bool] = []
    game_encryption_morse(words, morse_dict, answers)
    output_statistics(answers)


if __name__ == '__main__':
    main()
