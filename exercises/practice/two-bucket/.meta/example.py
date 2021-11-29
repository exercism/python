'''
    This solution implements a breadth-first search of the graph
    of possible valid states for the two buckets until it reaches a state
    in which one of the two buckets contains the goal amount
'''


def measure(bucket_one, bucket_two, goal, start_bucket):
    sizes = [bucket_one, bucket_two]
    goal_index = 0 if start_bucket == 'one' else 1

    def empty(buckets, idx):
        return [0, buckets[1]] if idx == 0 else [buckets[0], 0]

    def fill(buckets, idx):
        return [sizes[0], buckets[1]] if idx == 0 else [buckets[0], sizes[1]]

    def consolidate(buckets, idx):
        amount = min(buckets[1 - idx], sizes[idx] - buckets[idx])
        target = buckets[idx] + amount
        source = buckets[1 - idx] - amount
        return [target, source] if idx == 0 else [source, target]

    def bucket_str(buckets):
        return f'{buckets[0]},{buckets[1]}'

    invalid = [0, 0]
    invalid[1 - goal_index] = sizes[1 - goal_index]
    invalid_string = bucket_str(invalid)
    buckets = [0, 0]
    buckets[goal_index] = sizes[goal_index]
    to_visit = []
    visited = set()
    count = 1
    while goal not in buckets:
        key = bucket_str(buckets)
        if key != invalid_string and key not in visited:
            visited.add(key)
            number_count = count + 1
            for idx in range(2):
                if buckets[idx] != 0:
                    to_visit.append((empty(buckets, idx), number_count))
                if buckets[idx] != sizes[idx]:
                    to_visit.append((fill(buckets, idx), number_count))
                    to_visit.append((consolidate(buckets, idx), number_count))
        if not any(to_visit):
            raise ValueError('No more moves!')
        buckets, count = to_visit.pop(0)

    goal_index = buckets.index(goal)
    goal_bucket = ['one', 'two'][goal_index]
    other_bucket = buckets[1 - goal_index]
    return (count, goal_bucket, other_bucket)
