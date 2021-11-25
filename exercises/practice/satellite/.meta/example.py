def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError('traversals must have the same length')
    if set(preorder) != set(inorder):
        raise ValueError('traversals must have the same elements')
    if len(set(preorder)) != len(preorder) != len(set(inorder)):
        raise ValueError('traversals must contain unique items')
    if not preorder:
        return {}

    value = preorder.pop(0)
    index = inorder.index(value)
    left_inorder, right_inorder = inorder[:index], inorder[index+1:]

    left_preorder = [idx for idx in preorder if idx in left_inorder]
    right_preorder = [idx for idx in preorder if idx in right_inorder]

    left = tree_from_traversals(left_preorder, left_inorder)
    right = tree_from_traversals(right_preorder, right_inorder)

    return {'v': value, 'l': left, 'r': right}
