class StackUnderflowError(Exception):
    pass


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def evaluate(input_data):
    if not input_data:
        return []
    defines = {}
    while input_data[0][:1] == ':':
        values = input_data.pop(0).split()
        values.pop()
        values.pop(0)
        key = values.pop(0).lower()
        if is_integer(key):
            raise ValueError("Integers cannot be redefined")
        defines[key] = [
            x
            for v in values
            for x in defines.get(v, [v])
        ]
    stack = []
    input_data = input_data[-1].split()
    while any(input_data):
        word = input_data.pop(0).lower()
        try:
            if is_integer(word):
                stack.append(int(word))
            elif word in defines:
                input_data = defines[word] + input_data
            elif word == '+':
                stack.append(stack.pop() + stack.pop())
            elif word == '-':
                stack.append(-stack.pop() + stack.pop())
            elif word == '*':
                stack.append(stack.pop() * stack.pop())
            elif word == '/':
                divisor = stack.pop()
                if divisor == 0:
                    raise ZeroDivisionError("Attempted to divide by zero")
                stack.append(int(stack.pop() / divisor))
            elif word == 'dup':
                stack.append(stack[-1])
            elif word == 'drop':
                stack.pop()
            elif word == 'swap':
                stack.append(stack[-2])
                del stack[-3]
            elif word == 'over':
                stack.append(stack[-2])
            else:
                raise ValueError("{} has not been defined".format(word))
        except IndexError:
            raise StackUnderflowError("Insufficient number of items in stack")
    return stack
