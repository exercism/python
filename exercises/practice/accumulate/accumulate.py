def accumulate(collection, operation):
    result = []
    for item in collection:
        result.append(operation(item))
    return result
