NUMBERS = {10: "ten", 9: "nine", 8: "eight", 7: "seven", 6: "six", 5: "five", 4: "four", 3: "three", 2: "two", 1: "one", 0: "no"}

def recite(start, take=1):
    results = []
    for idx in range(start, start - take, -1):
        results.extend(verse(idx))
        if idx > start - take + 1:
            results.append('')
    return results


def verse(number):
    return [
        *main_verse(number),
        "And if one green bottle should accidentally fall,",
        last_verse(number)
        ]

def main_verse(number):
    if number == 1:
        return [
            f'One green bottle hanging on the wall,',
            f'One green bottle hanging on the wall,',
        ]
    else:
        return [
        f'{NUMBERS[number].capitalize()} green bottles hanging on the wall,',
        f'{NUMBERS[number].capitalize()} green bottles hanging on the wall,',]

def last_verse(number):
    if number -1 == 1:
        return f"There'll be one green bottle hanging on the wall."
    else:
        return f"There'll be {NUMBERS[number-1]} green bottles hanging on the wall."
