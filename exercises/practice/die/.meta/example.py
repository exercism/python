import random

def number_die(input=6):
    return random.randint(1, input)

def letter_die():
    return random.choice("abcdefghijklmnopqrstuvwxyz")
