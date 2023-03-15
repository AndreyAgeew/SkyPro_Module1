from typing import Dict


def get_name_user() -> str:
    """Функция получает и передает имя пользователя"""
    return str(input(f"Привет!\nПредлагаю проверить свои знания английского!"
                     f"\nРасскажи, как тебя зовут!\n"))


def database_of_questions(user_name: str) -> Dict:
    """Функция передает словарь из вопросов и ответов"""
    questions_dict: Dict = {
        f'My name __ {user_name}': 'is',
        'I __ a coder': 'am',
        'I Live __ Moscow': 'in'
    }
    return questions_dict


def quiz(user_name: str, questions: Dict) -> int:
    """
    Функция викторина
    :param user_name: имя пользователя
    :type: str
    :param questions: словарь с вопросами и ответами
    :type: dict
    points (int) - кол-во полученных баллов за правильные ответы (по default 0)
    :return: points
    """
    points: int = 0
    print(f'Привет, {user_name}, начнем тренировку!')
    for question, answer in questions.items():
        if str(input(f'Вопрос: {question}\nОтвет: ')) == answer:
            print(f'Ответ верный!\nВы получаете 10 баллов!\n')
            points += 10
        else:
            print(f'Неправильно.\nПравильный ответ: {answer}\n')
    return points


def output_results_quiz(user_name: str, points: int, questions: Dict) -> None:
    """Функция выводит результаты викторины"""
    print(f'Вот и всё, {user_name}!'
          f'\nВы ответили на {int(points / 10)} вопроса из {len(questions)} верно.'
          f'\nВы заработали {points} баллов.'
          f'\nЭто {round(100 / len(questions) * (points / 10), 1)} процентов')


def main() -> None:
    """
    Основная функция
    user_name (str) - передается имя пользователя
    questions (dict) - передается словарь из вопросов и ответов
    results_quiz (int) - передается результат в виде полученных баллов в викторине
        Functions:
            get_name_user - получает и передает имя пользователя
            database_of_questions - передает словарь из вопросов и ответов
            quiz - викторина (передает кол-во полученных баллов)
            output_results_quiz - выводит результаты викторины
    """
    user_name: str = get_name_user()
    questions: Dict = database_of_questions(user_name)
    results_quiz: int = quiz(user_name, questions)
    output_results_quiz(user_name, results_quiz, questions)


if __name__ == '__main__':
    main()
