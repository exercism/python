ROW = 4
COL = 3


def split_ocr(ocr):
    return [[ocr[i][COL * j:COL * (j + 1)] for i in range(ROW)]
            for j in range(len(ocr[0]) // COL)]


ALL = ['    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|',
       '                              ']

OCR_LIST = split_ocr(ALL)
OCR_LIST = [OCR_LIST[-1]] + OCR_LIST[:9]


def number(ocr):
    if (len(ocr) != ROW or len(ocr[0]) % COL or
            any(len(r) != len(ocr[0]) for r in ocr)):
        raise ValueError('Wrong grid size.')
    numbers = split_ocr(ocr)
    digits = ''
    for n in numbers:
        try:
            digits += str(OCR_LIST.index(n))
        except ValueError:
            digits += '?'
    return digits


def grid(digits):
    try:
        if not digits.isdigit():
            raise ValueError('String should be numeric.')
    except AttributeError:
        raise ValueError('Argument should be a string.')
    ocr = ['' for i in range(ROW)]
    for d in digits:
        for r in range(ROW):
            ocr[r] += OCR_LIST[int(d)][r]
    return ocr
