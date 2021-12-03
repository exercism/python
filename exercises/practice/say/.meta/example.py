def say(number):
    small = dict(enumerate((
            'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
            'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen')))

    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    kilo = 1e3
    mega = 1e6
    giga = 1e9
    tera = 1e12

    if number < 0:
        raise ValueError('input out of range')
    if number >= tera:
        raise ValueError('input out of range')

    if number < 20:
        return small[number]

    if number < 100:
        if number % 10 == 0:
            return tens[number]
        return tens[number // 10 * 10] + '-' + small[number % 10]

    if number < kilo:
        if number % 100 == 0:
            return small[number // 100] + ' hundred'
        return small[number // 100] + ' hundred ' + say(number % 100)

    if number < mega:
        if number % kilo == 0:
            return say(number // kilo) + ' thousand'
        return say(number // kilo) + ' thousand ' + say(number % kilo)

    if number < giga:
        if number % mega == 0:
            return say(number // mega) + ' million'
        return say(number // mega) + ' million ' + say(number % mega)

    if number % giga == 0:
        return say(number // giga) + ' billion'
    return say(number // giga) + ' billion ' + say(number % giga)