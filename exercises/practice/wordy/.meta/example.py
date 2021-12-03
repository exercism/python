from operator import add, mul, sub
from operator import floordiv as div


VALID_OPERATIONS = {'plus': add, 'minus': sub, 'multiplied by': mul, 'divided by': div}


def answer(question):
    if not bool(question[8:-1].strip().lower().split()):
        raise ValueError('syntax error')

    elif not question.startswith('What is '):
        raise ValueError('unknown operation')

    else:
        words = question[8:-1].strip().lower().split()
        words.reverse()

    try:
        main_value = int(words.pop())
    except ValueError as error:
        raise ValueError('syntax error') from error

    while words:
        operation = [words.pop()]
        while words:
            try:
                next_to_evaluate = words.pop()
                second_value = int(next_to_evaluate)
                break
            except ValueError as error:
                if next_to_evaluate == operation[-1]:
                    raise ValueError('syntax error') from error
                else:
                    operation.append(next_to_evaluate)
        else:
            if operation[-1] not in VALID_OPERATIONS and not operation[-1].isdigit() :
                raise ValueError('unknown operation')
            else:
                raise ValueError('syntax error')

        operation = ' '.join(operation)

        try:
            main_value = VALID_OPERATIONS[operation](main_value, second_value)
        except KeyError as error:
            raise ValueError('syntax error') from error

    return main_value
