from brain_games.scripts.cli import incorrect_answer, conditions
from brain_games.scripts.cli import welcome_user, congratulations
import prompt


def compare_answer(func_question, func_correct_answer, text_conditions):
    name = welcome_user()
    conditions(text_conditions)

    for i in range(3):
        question = func_question()
        correct_answer = func_correct_answer(question)

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            incorrect_answer(answer, correct_answer, name)
            return False

    congratulations(name)