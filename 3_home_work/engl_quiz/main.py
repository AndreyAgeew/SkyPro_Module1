from typing import List


def is_ready() -> None:
    """Функция проверят готовность"""
    if input('Привет! Предлагаю проверить свои '
             'знания английского! Наберите "ready", чтобы начать!\n') != 'ready':
        print('Кажется, вы не хотите играть. Очень жаль.')
        exit()


def get_name_user() -> str:
    """Функция получает и передает имя пользователя"""
    return str(input(f"Расскажи, как тебя зовут!\n"))


def database_of_questions(user_name: str) -> List[str]:
    """Функция передает список вопросов"""
    return [f'My name __ {user_name}', 'I __ a coder', 'I Live __ Moscow']


def database_of_answers() -> List[str]:
    """Функция передает список ответов"""
    return ['is', 'am', 'in']


def quiz(user_name: str, questions: List[str], answers: List[str]) -> int:
    """
    Функция викторина (передает результаты викторины)
    :param user_name: имя пользователя
    :type: str
    :param questions: список с вопросами
    :type: List[str]
    :param answers: список с ответами на вопрос
    :type: List[str]
    points (int) - кол-во полученных баллов за правильные ответы (по default 0)
    tmp_points (int) - кол-во баллов за один вопрос и кол-во попыток ответить на него (по default 3)
    amount_right_answers (int) - кол-во вопросов (используется для подсчета правильных ответов)
    :return: points, amount_questions
    """
    points: int = 0
    amount_right_answers: int = len(questions)

    print(f'Привет, {user_name}, начнем тренировку!')

    for i_question in range(len(questions)):
        tmp_points: int = 3
        while tmp_points >= 1:
            if str(input(f'Вопрос: {questions[i_question]}\nОтвет: ')).lower() == answers[i_question]:
                print(f'Ответ верный!\nВы получаете {tmp_points} баллов!\n')
                points += tmp_points
                break
            else:
                tmp_points -= 1
                if tmp_points:
                    print(f'Осталось попыток: {tmp_points}, попробуйте еще раз!')

        if tmp_points < 1:
            amount_right_answers -= 1
            print(f"Увы, но нет. Верный ответ: {answers[i_question]}\n")

    return points, amount_right_answers


def output_results_quiz(user_name: str, questions: List[str], points: int, right_answers: int) -> None:
    """Функция выводит результаты викторины"""
    print(f'Вот и всё, {user_name}!'
          f'\nВы ответили на {right_answers} вопроса из {len(questions)} верно.'
          f'\nЭто {round(100 / len(questions) * right_answers,1)} процентов'
          f'\nВы заработали {points} баллов.')


def main() -> None:
    """
    Основная функция
    user_name (str) - передается имя пользователя
    questions (List[str]) - передается список вопросов
    answers (List[str]) - передается список ответов
    results (List[int]) - передается результаты викторины [0] - кол-во баллов, [1] - кол-во правильных ответов
        Functions:
            is_ready - проверяет готовность к викторине
            database_of_questions - передает список вопросов
            database_of_answers - передает список ответов на вопросы
            quiz - викторина (передает результаты)
            output_results_quiz - выводит результаты викторины
    """
    is_ready()
    user_name: str = get_name_user().title()
    questions: List[str] = database_of_questions(user_name)
    answers: List[str] = database_of_answers()
    results: List[int] = quiz(user_name, questions, answers)
    output_results_quiz(user_name, questions, results[0], results[1])


if __name__ == '__main__':
    main()
