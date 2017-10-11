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


def two_bucket(bucket_one_cap, bucket_two_cap, desired_liters, first):
    if first == "one":
        moves = 0
        bucket_one, bucket_two = 0, 0
        while(True):
            if bucket_one == 0:
                moves += 1
                bucket_one = bucket_one_cap
            elif bucket_two == bucket_two_cap:
                moves += 1
                bucket_two = 0
            else:
                moves += 1
                measure = min(bucket_one, bucket_two_cap - bucket_two)
                bucket_one -= measure
                bucket_two += measure
            if bucket_one == desired_liters:
                return (moves, "one", bucket_two)
            elif bucket_two == desired_liters:
                return (moves, "two", bucket_one)

    elif first == "two":
        moves = 0
        bucket_one, bucket_two = 0, 0
        while(True):
            if bucket_two == 0:
                moves += 1
                bucket_two = bucket_two_cap
            elif bucket_one == bucket_one_cap:
                moves += 1
                bucket_one = 0
            else:
                moves += 1
                measure = min(bucket_two, bucket_one_cap - bucket_one)
                bucket_two -= measure
                bucket_one += measure
            if bucket_one == desired_liters:
                return (moves, "one", bucket_two)
            elif bucket_two == desired_liters:
                return (moves, "two", bucket_one)
