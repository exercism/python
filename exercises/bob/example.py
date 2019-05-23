def response(hey_bob):
    hey_bob = hey_bob.strip()

    if _is_silence(hey_bob):
        return 'Fine. Be that way!'
    if _is_shouting(hey_bob):
        if _is_question(hey_bob):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'
    elif _is_question(hey_bob):
        return 'Sure.'
    else:
        return 'Whatever.'


def _is_silence(hey_bob):
    return hey_bob == ''


def _is_shouting(hey_bob):
    return hey_bob.isupper()


def _is_question(hey_bob):
    return hey_bob.endswith('?')
