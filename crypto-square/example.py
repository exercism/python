import math


def encode(msg):
    msg = _cleanse(msg)
    sqrsz = int(math.sqrt(len(msg)))
    if sqrsz * sqrsz < len(msg):
        sqrsz += 1

    cols = [msg[i1::sqrsz] for i1 in range(sqrsz)]
    cols_str = ''.join(cols)
    return ' '.join(cols_str[i1:i1 + 5] for i1 in range(0, len(cols_str), 5))


def decode(ciph):
    ciph = _cleanse(ciph)
    sqrsz = int(math.sqrt(len(ciph)))
    if sqrsz * sqrsz < len(ciph):
        sqrsz += 1
    colsz, nbr_full_cols = divmod(len(ciph), sqrsz)

    # The matrix produced by the plaintext is in general irregular, and the
    # last row is usually shorter than the others. Extract this row first
    full_cols_str = ciph[:(colsz + 1) * nbr_full_cols]
    partial_cols_str = ciph[(colsz + 1) * nbr_full_cols:]
    last_row = full_cols_str[colsz::colsz + 1]

    # Compute the string of all concatenated columns of the colsz X sqrsz
    # matrix consisting of the first colsz rows of the plaintext (irregular)
    # matrix
    trimmed_full_cols = [full_cols_str[i1:i1 + colsz]
                         for i1 in range(0, len(full_cols_str), colsz + 1)]
    partial_cols = [partial_cols_str[i1:i1 + colsz]
                    for i1 in range(0, len(partial_cols_str), colsz)]
    uniform_cols_str = ''.join(trimmed_full_cols + partial_cols)

    other_rows = [uniform_cols_str[i1::colsz] for i1 in range(colsz)]
    return ''.join(other_rows + [last_row])


def _cleanse(s):
    """Lowercase a string and remove punctuation and whitespace
    """
    return ''.join([c for c in s if c.isalnum()]).lower()


if __name__ == '__main__':
    msg = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
    ciph = 'imtgd vsfea rwerm ayoog oanou uiont nnlvt wttdd esaoh ghnss eoau'
    print(encode(msg))
    print(decode(ciph))
