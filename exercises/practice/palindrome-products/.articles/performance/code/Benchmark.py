import timeit
import sys


print(sys.version)


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b >= result:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)

def largest_optimized(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(max_factor, min_factor - 1,-1):
        was_bigger = False
        for number_b in range(max_factor, number_a - 1, -1):
            if number_a * number_b >= result:
                was_bigger = True
                test_value  = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_bigger:
            break
    if result == 0:
        result = None
    return (result, answer)


def smallest_optimized(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        was_smaller = False
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                was_smaller = True
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_smaller:
            break
    if result == 0:
        result = None
    return (result, answer)


starttime = timeit.default_timer()
largest(1, 1000)
print("largest, min=1, max=1000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
largest_optimized(1, 1000)
print("largest_optimized, min=1, max=1000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
smallest(1, 1000)
print("smallest, min=1, max=1000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
smallest_optimized(1, 1000)
print("smallest_optimized, min=1, max=1000 :", timeit.default_timer() - starttime)



starttime = timeit.default_timer()
largest(100, 100000)
print("largest, min=100, max=100000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
largest_optimized(100, 100000)
print("largest_optimized, min=100, max=100000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
smallest(100, 100000)
print("smallest, min=100, max=100000 :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
smallest_optimized(100, 100000)
print("smallest_optimized, min=100, max=100000 :", timeit.default_timer() - starttime)
