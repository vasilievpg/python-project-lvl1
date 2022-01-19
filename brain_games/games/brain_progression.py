from random import randint

text_conditions = "What number is missing in the progression?"


def get_question_and_answer():
    start = randint(1, 100)
    step = randint(1, 10)
    length_progression = randint(5, 10)

    progression = [str(start + i * step) for i in range(length_progression)]

    hidden_element_num = randint(0, length_progression - 1)
    hidden_element = progression[hidden_element_num]
    progression[hidden_element_num] = ".."
    question = " ".join(str(e) for e in progression)

    return question, str(hidden_element)
