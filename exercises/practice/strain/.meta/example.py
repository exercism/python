def keep(sequence, predicate):
    return [element for element in sequence if predicate(element)]

def discard(sequence, predicate):
    return [element for element in sequence if not predicate(element)]
