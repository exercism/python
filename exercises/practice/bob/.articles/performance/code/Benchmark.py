import timeit

loops = 1_000_000

val = timeit.timeit("""response("I really don't have anything to say.")""",
                    """
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    isShout = hey_bob.isupper()
    isQuestion = hey_bob.endswith('?')
    if isShout and isQuestion:
        return "Calm down, I know what I'm doing!"
    if isShout:
        return 'Whoa, chill out!'
    if isQuestion:
        return 'Sure.'
    return 'Whatever.'

""", number=loops) / loops

print(f"if statements: {val}")


val = timeit.timeit("""response("I really don't have anything to say.")""",
                    """
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    isShout = hey_bob.isupper()
    isQuestion = hey_bob.endswith('?')
    if isShout:
        if isQuestion:
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'    
    if isQuestion:
        return 'Sure.'
    return 'Whatever.'

""", number=loops) / loops

print(f"if statements nested: {val}")

val = timeit.timeit("""response("I really don't have anything to say.")""",
                    """

_ANSWERS = ["Whatever.", "Sure.", "Whoa, chill out!", "Calm down, I know what I'm doing!"]

def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob: return 'Fine. Be that way!'
    isShout = 2 if hey_bob.isupper() else 0
    isQuestion = 1 if hey_bob.endswith('?') else 0
    return _ANSWERS[isShout + isQuestion]
    

""", number=loops) / loops

print(f"answer array: {val}")
