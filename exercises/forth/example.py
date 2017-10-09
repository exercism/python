def is_integer(string):
    try:
        int(string)
        return True
    except:
        return False


def evaluate(input_data):
    defines = {}
    while input_data[0][0] == ':':
        values = input_data.pop(0).split()
        values.pop()
        values.pop(0)
        key = values.pop(0)
        if is_integer(key):
            return None
        defines[key] = values
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
                divider = stack.pop()
                stack.append(int(stack.pop() / divider))
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
                return None
        except:
            return None
    return stack
