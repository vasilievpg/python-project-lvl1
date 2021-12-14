from brain_games.scripts.cli import welcome_user
import prompt


def compare_answer(func_answer, text_conditions):
    name = welcome_user()
    print(text_conditions)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = func_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False

    print(f"Congratulations, {name}!")