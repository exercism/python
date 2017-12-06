def is_armstrong(number):
    return sum(pow(int(digit), len(str(number))) for digit in str(number)) == number
