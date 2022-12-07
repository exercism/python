import timeit

loops = 1_000_000

val = timeit.timeit("""response("I really don't have anything to say.")""",
                    """
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_shout and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shout:
        return 'Whoa, chill out!'
    if is_question:
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
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    if is_question:
        return 'Sure.'
    return 'Whatever.'

""", number=loops) / loops

print(f"if statements nested: {val}")

val = timeit.timeit("""response("I really don't have anything to say.")""",
                    """

ANSWERS = ['Whatever.', 'Sure.', 'Whoa, chill out!',
            "Calm down, I know what I'm doing!"]


def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = 2 if hey_bob.isupper() else 0
    is_question = 1 if hey_bob.endswith('?') else 0
    return ANSWERS[is_shout + is_question]
    

""", number=loops) / loops

print(f"answer list: {val}")
