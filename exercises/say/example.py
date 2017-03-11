def say(number, recursive=False):
    small = dict(enumerate((
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')))

    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    k, m, b, t = 1e3, 1e6, 1e9, 1e12

    if number < 0:
        raise AttributeError('number is negative')
    if number >= t:
        raise AttributeError('number is too large: %s' % str(number))

    if number < 20:
        return small[number] if not recursive else 'and ' + small[number]

    if number < 100:
        if number % 10 == 0:
            return small[number]
        return tens[number // 10 * 10] + '-' + small[number % 10]

    if number < k:
        if number % 100 == 0:
            return small[number // 100] + ' hundred'
        return small[number // 100] + ' hundred and ' + say(number % 100)

    if number < m:
        if number % k == 0:
            return say(number // k) + ' thousand'
        return say(number // k) + ' thousand ' + say(number % k, True)

    if number < b:
        if number % m == 0:
            return say(number // m) + ' million'
        return say(number // m) + ' million ' + say(number % m, True)

    if number % b == 0:
        return say(number // b) + ' billion'
    return say(number // b) + ' billion ' + say(number % b, True)
