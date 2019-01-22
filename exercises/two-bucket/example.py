'''
    This solution implements a breadth-first search of the graph
    of possible valid states for the two buckets until it reaches a state
    in which one of the two buckets contains the goal amount
'''


def measure(bucket_one, bucket_two, goal, start_bucket):
    sizes = [bucket_one, bucket_two]
    goal_index = 0 if start_bucket == 'one' else 1

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
    invalid[1 - goal_index] = sizes[1 - goal_index]
    invalid_str = bucket_str(invalid)
    buckets = [0, 0]
    buckets[goal_index] = sizes[goal_index]
    to_visit = []
    visited = set()
    count = 1
    while goal not in buckets:
        key = bucket_str(buckets)
        if key != invalid_str and key not in visited:
            visited.add(key)
            nc = count + 1
            for i in range(2):
                if buckets[i] != 0:
                    to_visit.append((empty(buckets, i), nc))
                if buckets[i] != sizes[i]:
                    to_visit.append((fill(buckets, i), nc))
                    to_visit.append((consolidate(buckets, i), nc))
        if not any(to_visit):
            raise ValueError('No more moves!')
        buckets, count = to_visit.pop(0)

    goal_index = buckets.index(goal)
    goal_bucket = ['one', 'two'][goal_index]
    other_bucket = buckets[1 - goal_index]
    return (count, goal_bucket, other_bucket)
