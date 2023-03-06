from typing import Dict


def get_name_user() -> str:
    """Функция получает и передает имя пользователя"""
    return str(input('Как тебя зовут?'))


def is_ready(user_name) -> None:
    """Функция проверяет ввод ready"""
    print(f'Привет, {user_name}! Предлагаю проверить свои знания английского')
    while True:
        if str(input('Введите "ready":')).lower() == "ready":
            break


def database_of_questions(user_name: str) -> Dict:
    """Функция передает словарь из вопросов и ответов"""
    questions_dict: Dict = {
        f'My name __ {user_name}': 'is',
        'I __ a coder': 'am',
        'I Live __ Moscow': 'in'
    }
    return questions_dict


def quiz(questions: Dict) -> int:
    """
    Функция викторина
    :param questions: словарь с вопросами и ответами
    :type: dict
    points (int) - кол-во правильных ответов(по default 0)
    :return: points
    """
    points: int = 0
    for question, answer in questions.items():
        if str(input(f'Вопрос: {question}\nОтвет: ')) == answer:
            print(f'Ответ верный!\n')
            points += 1
        else:
            print(f'Неправильно.\nПравильный ответ: {answer}\n')
    return points


def output_results_quiz(user_name: str, points: int, questions: Dict) -> None:
    """Функция выводит результаты викторины"""
    print(f'Вот и всё, {user_name}!'
          f'\nВы ответили на {int(points)} вопроса из {len(questions)} верно.'
          f'\nЭто {round(100 / len(questions) * points, 1)} процентов')


def main() -> None:
    """
    Основная функция
    user_name (str) - передается имя пользователя
    questions (dict) - передается словарь из вопросов и ответов
    results_quiz (int) - передается результат в виде полученных баллов в викторине
        Functions:
            get_name_user - получает и передает имя пользователя
            is_ready - проверяет готовность
            database_of_questions - передает словарь из вопросов и ответов
            quiz - викторина (передает кол-во полученных баллов)
            output_results_quiz - выводит результаты викторины
    """
    user_name: str = get_name_user()
    is_ready(user_name)
    questions: Dict = database_of_questions(user_name)
    results_quiz: int = quiz(questions)
    output_results_quiz(user_name, results_quiz, questions)


if __name__ == '__main__':
    main()
