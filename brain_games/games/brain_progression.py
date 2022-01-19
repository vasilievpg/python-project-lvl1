from random import randint

text_conditions = "What number is missing in the progression?"


def get_question_and_answer():
    start = randint(1, 100)
    difference = randint(1, 10)
    length_progression = randint(5, 10)
    progression = [
        start,
    ]
    last_element = start

    for _ in range(length_progression):
        last_element = last_element + difference
        progression.append(last_element)

    hidden_element_num = randint(0, length_progression - 1)
    hidden_element = progression[hidden_element_num]
    progression[hidden_element_num] = ".."
    question = " ".join(str(e) for e in progression)

    return question, str(hidden_element)
