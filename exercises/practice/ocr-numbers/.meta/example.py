NUM_ROWS = 4
NUM_COLS = 3


def split_ocr(ocr):
    return [[ocr[idx][NUM_COLS * jam:NUM_COLS * (jam + 1)] for idx in range(NUM_ROWS)]
            for jam in range(len(ocr[0]) // NUM_COLS)]


ALL = ['    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|',
       '                              ']

OCR_LIST = split_ocr(ALL)
OCR_LIST = [OCR_LIST[-1]] + OCR_LIST[:9]


def convert(input_grid):
    split_indices = (list(range(0, len(input_grid), NUM_ROWS)) +
                     [len(input_grid)])

    lines = [input_grid[start:end]
             for start, end in zip(split_indices[:-1], split_indices[1:])]

    return ','.join(convert_one_line(line) for line in lines)


def convert_one_line(input_grid):
    if len(input_grid) != NUM_ROWS:
        raise ValueError('Number of input lines is not a multiple of four')

    if len(input_grid[0]) % NUM_COLS:
        raise ValueError('Number of input columns is not a multiple of three')

    numbers = split_ocr(input_grid)
    digits = ''
    for num in numbers:
        try:
            digits += str(OCR_LIST.index(num))
        except ValueError:
            digits += '?'
    return digits
