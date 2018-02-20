'''
    This solution implements a breadth-first search of the graph
    of possible valid states for the two buckets until it reaches a state
    in which one of the two buckets contains the goal amount
'''


def measure(bucket_one, bucket_two, goal, start_bucket):
    sizes = [bucket_one, bucket_two]
    goalIndex = 0 if start_bucket == 'one' else 1

    def empty(buckets, i):
        return [0, buckets[1]] if i == 0 else [buckets[0], 0]

    def fill(buckets, i):
        return [sizes[0], buckets[1]] if i == 0 else [buckets[0], sizes[1]]

    def consolidate(buckets, i):
        amount = min(buckets[1 - i], sizes[i] - buckets[i])
        target = buckets[i] + amount
        src = buckets[1 - i] - amount
        return [target, src] if i == 0 else [src, target]

    def bucket_str(buckets):
        return '{},{}'.format(*buckets)

    invalid = [0, 0]
    invalid[1 - goalIndex] = sizes[1 - goalIndex]
    invalidStr = bucket_str(invalid)
    buckets = [0, 0]
    buckets[goalIndex] = sizes[goalIndex]
    toVisit = []
    visited = set()
    count = 1
    while goal not in buckets:
        key = bucket_str(buckets)
        if key != invalidStr and key not in visited:
            visited.add(key)
            nc = count + 1
            for i in range(2):
                if buckets[i] != 0:
                    toVisit.append((empty(buckets, i), nc))
                if buckets[i] != sizes[i]:
                    toVisit.append((fill(buckets, i), nc))
                    toVisit.append((consolidate(buckets, i), nc))
        if not any(toVisit):
            raise ValueError('No more moves!')
        buckets, count = toVisit.pop(0)

    goalIndex = buckets.index(goal)
    goalBucket = ['one', 'two'][goalIndex]
    otherBucket = buckets[1 - goalIndex]
    return (count, goalBucket, otherBucket)
