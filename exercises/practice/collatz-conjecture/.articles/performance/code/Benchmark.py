import timeit

def steps_if(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        counter += 1
    return counter

def steps_recursion(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return 1 + steps_recursion(number)

def steps_ternary(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        counter += 1
    return counter


starttime = timeit.default_timer()
steps_recursion(100000)
print("Steps with recursion :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
steps_ternary(100000)
print("Steps with ternary :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
steps_if(100000)
print("Steps with if/else :", timeit.default_timer() - starttime)
