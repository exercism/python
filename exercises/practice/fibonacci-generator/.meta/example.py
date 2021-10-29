
def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
