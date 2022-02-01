import prompt

NUMBER_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    if game is None:
        return

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
