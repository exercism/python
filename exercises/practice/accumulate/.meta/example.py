# [collection(x) for x in collection] would be nice but trivial


def accumulate(collection, operation):
    response = []
    for element in collection:
        response.append(operation(element))
    return response
