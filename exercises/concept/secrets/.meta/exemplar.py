def secret_add(secret):
    return lambda addend: secret + addend

def secret_multiply(secret):
    return lambda multiplicand: secret * multiplicand

def secret_max(secret):
    return lambda num: max(secret, num, key=lambda l: l[0] * l[1])

def secret_sort(secret_index):
    return lambda l: sorted(l, key=lambda x: x[secret_index])

def secret_combine(secret_function1, secret_function2):
    return lambda x: secret_function2(secret_function1(x))
