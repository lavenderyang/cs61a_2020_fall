# tree

# constructor 
def tree(label, branches=[]):
    """
    >>> t = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])
    >>> t
    [1, [3, [4], [5], [6]], [2]]
    """
    for branch in branches: 
        assert is_tree(branch), 'branches must be trees.'
    return [label] + list(branches)

# selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1: 
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)




### +++ === ABSTRACTION BARRIER === +++ ###

# Height
def height(tree):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(tree):
        return 0
    else: 
        return 1 + max([height(branch) for branch in branches(tree)])


def print_tree(tree, indent=0):
    """Print a representation of this tree in which each label is indented by two spaces times its depth from the root. 
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    """
    print('  ' * indent + str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent + 1)



