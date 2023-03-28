def is_enter() -> bool:
    """Функция проверяет нажатия Enter (без ввода значений)"""
    while True:
        if input('Нажмите Enter') == '':
            return True


def database_words() -> dict[str:str]:
    """Функция передает словарь из слов - перевод разных сложностей"""
    words_dict: dict[str:str] = {
        'лёгкий': {
            'people': 'люди',
            'husband': 'муж',
            'friend': 'друг',
            'head': 'голова',
            'name': 'имя'
        },
        'средний': {
            'Phenomenon': 'феномен',
            'Regularly': 'регулярно',
            'February': 'февраль',
            'Aluminium': 'алюминий',
            'Statistics': 'статистика'

        },
        'сложный': {
            'Hospitable': 'гостеприимный',
            'Prejudice': 'предубеждение',
            'Remuneration': 'вознаграждение',
            'Thesaurus': 'словарь',
            'Invulnerability': 'неуязвимость'
        }
    }
    return words_dict


def database_ranks() -> dict[int:str]:
    """Функция передает словарь из рангов"""
    ranks_dict: dict[int:str] = {
        0: 'Нулевой',
        1: 'Так себе',
        2: 'Можно лучше',
        3: 'Норм',
        4: 'Хорошо',
        5: 'Отлично'
    }
    return ranks_dict


def quiz(words_dict: dict[str:str], correct_answers_dict: dict[str:str]) -> None:
    """
    Функция викторина (передает в словарь ответов, какие правильные, а какие нет)
    :param words_dict: словарь со словами (3-х сложностей)
    :type: Dict
    :param correct_answers_dict: словарь из 2-х списков (правильные и неправильные ответы)
    :type: Dict
    user_level (str) - передается уровень сложности, выбранный пользователем
    """
    while True:
        user_level = str(input('Выберите уровень сложности\n'
                               'Лёгкий, средний, сложный\n')).lower()
        if user_level in words_dict:
            print(f'Выбран уровень сложности, мы предложим {len(words_dict[user_level])} слов, '
                  f'подберите перевод')
            for key, value in words_dict[user_level].items():
                is_enter()
                print(f'{key.lower()}, {len(value)} букв, начинается на {value[0]}...')
                if str(input('')).lower() == value:
                    print(f'Верно, {key}, это {value}')
                    correct_answers_dict['correctly'].append(key.lower())
                else:
                    print(f'Неверно, {key}, это {value}')
                    correct_answers_dict['not_correctly'].append(key.lower())
            break


def output_results_quiz(correct_answers_dict: dict[str:str], ranks: dict[int:str]) -> None:
    """
    Функция выводит результаты викторины
    :param correct_answers_dict: словарь с 2-мя списками (правильные и неправильные ответы)
    :type: Dict
    :param ranks: словарь рангов
    :type: Dict
    """
    print()
    if not len(correct_answers_dict['correctly']):
        print(f'Вы не смогли дать ответ ни на 1 слово!\n'
              f"Ваш ранг '{ranks[len(correct_answers_dict['correctly'])]}'")
    elif len(correct_answers_dict['correctly']) and len(correct_answers_dict['not_correctly']):
        print('Правильно отвечены слова:')
        for key in correct_answers_dict['correctly']:
            print(key)
        print()
        print('Неправильно отвечены слова:')
        for key in correct_answers_dict['not_correctly']:
            print(key)
        print(f"Ваш ранг '{ranks[len(correct_answers_dict['correctly'])]}'")
    else:
        print(f"Вы отгадали все слова!\n"
              f"Ваш ранг '{ranks[len(correct_answers_dict['correctly'])]}'")


def main() -> None:
    """
    words (Dict) - передается словарь слов (3 словаря разных сложностей)
    ranks (Dict) - передается словарь рангов
    answers (Dict) - передается словарь из 2-х списков (правильные и неправильные ответы)
        Functions:
            quiz - викторина передает правильные и неправильные ответы в answers
            output_results_quiz - выводит результаты викторины
    """
    words: dict[str:str] = database_words()
    ranks: dict[int:str] = database_ranks()
    answers: dict[str:str] = {
        'correctly': [],
        'not_correctly': []
    }
    quiz(words, answers)
    output_results_quiz(answers, ranks)


if __name__ == '__main__':
    main()
