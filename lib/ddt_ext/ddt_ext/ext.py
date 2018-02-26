from ddt import idata
from inspect import getargspec


class AnnotatedCase(dict):
    pass


def create_case(name, case_args, *args):
    case = AnnotatedCase()
    for k, v in zip(case_args, args):
        case[k] = v
    setattr(case, '__name__', name)
    return case


def annotated_data(**kwargs):
    def dec(function):
        @idata(
            create_case(
                k,
                [p for p in getargspec(function)[0] if p != 'self'],
                *v
            )
            for k, v in kwargs.items()
        )
        def wrapper(*args, **kwargs):
            function(args[0], **args[1])
        return wrapper
    return dec
