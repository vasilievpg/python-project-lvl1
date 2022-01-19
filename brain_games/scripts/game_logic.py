import prompt

NUMBER_OF_ROUNDS = 3


def game_logic(game_mod):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}?')

    print(game_mod.text_conditions)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game_mod.get_question_and_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")