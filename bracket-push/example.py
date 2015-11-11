def check_brackets(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in string:
        if char in counterparts.values():
            stack.append(char)
        elif char in counterparts:
            if not stack:
                return False
            if stack.pop() != counterparts[char]:
                return False
    return not stack
