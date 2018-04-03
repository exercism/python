def hey(stimulus):
    stimulus = stimulus.strip()

    if _is_silence(stimulus):
        return 'Fine. Be that way!'
    if _is_shouting(stimulus):
        if _is_question(stimulus):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'
    elif _is_question(stimulus):
        return 'Sure.'
    else:
        return 'Whatever.'


def _is_silence(stimulus):
    return stimulus == ''


def _is_shouting(stimulus):
    return stimulus.isupper()


def _is_question(stimulus):
    return stimulus.endswith('?')
