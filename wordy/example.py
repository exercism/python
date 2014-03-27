from operator import add, div, mul, sub

VALID_OPERATIONS = {"plus": add, "minus": sub, "times": mul, 
                    "multiplied by": mul, "divided by": div}

def calculate(stmt):
    if not (stmt.startswith("What is ") and stmt.endswith("?")):
        raise ValueError("Ill-formed question")
    l = stmt[8:-1].strip().lower().split()
    if not l:
        raise ValueError("Ill-formed question")
    l.reverse()
    try:
        op1 = int(l.pop())
    except ValueError:
        raise ValueError("Ill-formed question")
    while l:
        oprt = [l.pop()]
        while l:
            try:
                next_tk = l.pop()
                op2 = int(next_tk)
                break
            except ValueError:
                oprt.append(next_tk)
        else:
            raise ValueError("Ill-formed question")
        oprt = " ".join(oprt)
        try:
            op1 = VALID_OPERATIONS[oprt](op1, op2)
        except KeyError:
            raise ValueError("Ill-formed question")
    return op1