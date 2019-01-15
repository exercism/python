def TreeFromTraversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder) != len(set(inorder)):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    value = preorder.pop(0)
    index = inorder.index(value)
    lio, rio = inorder[:index], inorder[index+1:]
    left = TreeFromTraversals([x for x in preorder if x in lio], lio)
    right = TreeFromTraversals([x for x in preorder if x in rio], rio)
    return {"v": value, "l": left, "r": right}
