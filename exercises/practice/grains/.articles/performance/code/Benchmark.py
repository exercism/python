import timeit

loops = 1_000_000

val = timeit.timeit("""square(64)""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)

def total():
    return (1 << 64) - 1

""", number=loops) / loops

print(f"bit shifting square 64:   {val}")


val = timeit.timeit("""total()""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)

def total():
    return (1 << 64) - 1

""", number=loops) / loops

print(f"bit shifting total 64:    {val}")

val = timeit.timeit("""square(64)""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    return 2**(number - 1)
    
def total():
    return 2**64 - 1

""", number=loops) / loops

print(f"exponentiation square 64: {val}")


val = timeit.timeit("""total()""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    return 2**(number - 1)
    
def total():
    return 2**64 - 1

""", number=loops) / loops

print(f"exponentiation total 64:  {val}")

val = timeit.timeit("""square(64)""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    return pow(2, number-1)
    
def total():
    return pow(2, 64) - 1

""", number=loops) / loops

print(f"pow square 64:            {val}")


val = timeit.timeit("""total()""",
                    """
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    return pow(2, number-1)
    
def total():
    return pow(2, 64) - 1

""", number=loops) / loops

print(f"pow total 64:             {val}")
