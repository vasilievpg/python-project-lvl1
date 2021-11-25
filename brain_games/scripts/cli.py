import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}?')
    return name


def conditions(text):
    print(text)


def congratulations(name):
    print(f"Congratulations, {name}!")


def incorrect_answer(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer ;(. ", end='')
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def compare_answer(question, correct_answer, name):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        incorrect_answer(answer, correct_answer, name)
        return False
