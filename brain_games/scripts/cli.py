import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}?')
    return name


def incorrect_answer(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")

