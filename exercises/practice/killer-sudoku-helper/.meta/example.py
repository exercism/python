import itertools

def combinations(target, size, exclude):
    possible = [i for i in range(1, target) if i not in exclude]
    result = [seq for i in range(len(possible), 0, -1)
          for seq in itertools.combinations(possible, i)
          if sum(seq) == target]

  
    return result
