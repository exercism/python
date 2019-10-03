import sys
from operator import add, mul, sub

if sys.version_info[0] == 2:
    from operator import div
else:
    from operator import floordiv as div


VALID_OPERATIONS = {"plus": add, "minus": sub,
                    "multiplied by": mul, "divided by": div}


def answer(question):
    if not (question.startswith("What is ") and question.endswith("?")):
        raise ValueError("Ill-formed question")
    words = question[8:-1].strip().lower().split()
    if not words:
        raise ValueError("Ill-formed question")
    words.reverse()
    try:
        main_value = int(words.pop())
    except ValueError:
        raise ValueError("Ill-formed question")
    while words:
        operation = [words.pop()]
        while words:
            try:
                next_to_evaluate = words.pop()
                second_value = int(next_to_evaluate)
                break
            except ValueError:
                operation.append(next_to_evaluate)
        else:
            raise ValueError("Ill-formed question")
        operation = " ".join(operation)
        try:
            main_value = VALID_OPERATIONS[operation](main_value, second_value)
        except KeyError:
            raise ValueError("Ill-formed question")
    return main_value
