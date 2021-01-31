NUM_ROWS = 4
NUM_COLS = 3


def split_ocr(ocr):
    return [[ocr[i][NUM_COLS * j:NUM_COLS * (j + 1)] for i in range(NUM_ROWS)]
            for j in range(len(ocr[0]) // NUM_COLS)]


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

    return ",".join(convert_one_line(line) for line in lines)


def convert_one_line(input_grid):
    if (len(input_grid) != NUM_ROWS or len(input_grid[0]) % NUM_COLS or
            any(len(r) != len(input_grid[0]) for r in input_grid)):
        raise ValueError('Wrong grid size.')
    numbers = split_ocr(input_grid)
    digits = ''
    for n in numbers:
        try:
            digits += str(OCR_LIST.index(n))
        except ValueError:
            digits += '?'
    return digits
