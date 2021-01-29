def is_armstrong_number(number):
    return sum(pow(int(d), len(str(number))) for d in str(number)) == number
