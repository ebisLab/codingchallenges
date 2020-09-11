#
# Binary trees are already defined with this interface:


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def tree_paths_sum(root):
    # need to figure out which sweep/tree traversal method to use -> pre order
    # need to find sum
    if not root:  # if its empty
        return 0
    # utilizing recursion
    else:
        return tree_paths_sum(root.left)+tree_paths_sum(root.right)+root.value


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sum = addBT(root)

    print("Sum of all the nodes is:", sum)
