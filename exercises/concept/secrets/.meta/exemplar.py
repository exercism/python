def secret_add(secret):
    """
    Return a lambda that adds the argument from the lambda to the argument passed into secret_add.
    
    :param secret: secret number to add (integer)
    :return: lambda that takes a number and adds it to the secret
    """
    return lambda addend: secret + addend

def secret_multiply(secret):
    """
    Return a lambda that multiplies the argument from the lambda to the argument passed into secret_multiply.
    
    :param secret: secret number to multiply (integer)
    :return: lambda that takes a number and multiplies it to the secret
    """
    return lambda multiplicand: secret * multiplicand

def secret_max(secret):
    """
    Return a lambda that returns either the argument from the lambda or the argument passed in to secret_max, whichever one's product is bigger.
    
    :param secret: secret list of two numbers (list)
    :return: lambda that takes a list of two numbers
    """
    return lambda num: max(secret, num, key=lambda l: l[0] * l[1])

def secret_sort(secret_index):
    """
    Return a lambda that takes one argument, a list of lists of an unknown amount of numbers. The lambda should return the list of lists, but sorted by sublist[secret_index].
    
    :param secret_index: secret index to sort by (integer)
    :return: lambda that takes a list of lists of numbers and sorts them
    """
    return lambda l: sorted(l, key=lambda x: x[secret_index])

def secret_combine(secret_function1, secret_function2):
    """
    Return a lambda that takes one argument and applies to it the two functions passed in to secret_combine in order.

    :param secret_function1: function
    :param secret_function2: function
    :return: lambda that composes the two functions
    """
    return lambda x: secret_function2(secret_function1(x))
