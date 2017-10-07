'''
The solution follows the following approach:

->Pour from first bucket to second
  1.Fill the first bucket and empty it into the second bucket.
  2.If first bucket is empty fill it.
  3.If the second bucket is full empty it.
  4.Repeat steps 1,2,3 till either the first or second bucket contains the
    desired amount.

->Pour from first bucket to second
  1.Fill the second bucket and empty it into the first bucket.
  2.If second bucket is empty fill it.
  3.If the firts bucket is full empty it.
  4.Repeat steps 1,2,3 till either the first or second bucket contains the
    desired amount.
'''


def two_bucket(bucket_one, bucket_two, d, first):
    if first == "one":
        count = 0
        m, n = 0, 0
        while(True):
            if m == 0:
                count += 1
                m = bucket_one
            elif n == bucket_two:
                count += 1
                n = 0
            else:
                count += 1
                measure = min(m, bucket_two - n)
                m -= measure
                n += measure
            if m == d:
                return (count, "one", n)
            elif n == d:
                return (count, "two", m)

    elif first == "two":
        count = 0
        m, n = 0, 0
        while(True):
            if n == 0:
                count += 1
                n = bucket_two
            elif m == bucket_one:
                count += 1
                m = 0
            else:
                count += 1
                measure = min(n, bucket_one - m)
                n -= measure
                m += measure
            if m == d:
                return (count, "one", n)
            elif n == d:
                return (count, "two", m)
