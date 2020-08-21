"""queue data structure, we can go back to the prev nodes and get its child nodes"""
"""
its better to not use array but to use LL

space complexity o(height of the tree)
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        # return f"value: {self.value} left: {self.left} right: {self.right}"
        return "{}".format(self.value)


class BST():
    def __init__(self):
        self.root = None
        self.node_nums = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.node_nums += 1
        else:
            current_node = self.root  # we're going to have to traverse this node
            # self.root = new_node
            # self.node_nums += 1

            # we don't know how long we have to traverse it for
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.value > current_node.value:
                    # go right
                    # is there's nothing next to it on the right of it
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.value < current_node.value:
                    # go left
                    # is there something to the left of our current node
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
                self.node_nums += 1
                return

    def lookup(self, value):
        if self.root == None:
            print("empty")
        else:
            current_node = self.root
            # we need to traverse
            while True:  # current_node is true
                if current_node is None:
                    print("Not found")
                    return "Not Found"
                if current_node.value == value:
                    print(f"* {current_node.value} * Found")
                    return "Found"
                elif current_node.value > value:
                    # go left
                    current_node = current_node.left
                elif current_node.value < value:
                    # go right
                    current_node = current_node.right

    def dfs_inorder(self):
        return traversal_inorder(self.root, [])

    def dfs_postorder(self):
        return traversal_postorder(self.root, [])

    def dfs_preorder(self):
        return traversal_preorder(self.root, [])


def traversal_inorder(node, DFS_list):
    print("in order", node.value)
    # does the node  have a left child
    if node.left:
        # traverse all the way down until node has no more children
        traversal_inorder(node.left, DFS_list)
    # when no more node.left
    DFS_list.append(node.value)

    if node.right:
        traversal_inorder(node.right, DFS_list)
    return DFS_list


def traversal_postorder(node, DFS_list):
    print("post order", node.value)
    # does the node  have a left child
    if node.left:
        # traverse all the way down until node has no more children
        traversal_postorder(node.left, DFS_list)
    # when no more node.left

    if node.right:
        traversal_postorder(node.right, DFS_list)

    DFS_list.append(node.value)

    # push at the very end
    return DFS_list


def traversal_preorder(node, DFS_list):
    print("preorder", node.value)
    # push at  the very beginning
    DFS_list.append(node.value)
    # does the node  have a left child

    if node.left:
        # traverse all the way down until node has no more children
        traversal_preorder(node.left, DFS_list)
    # when no more node.left

    if node.right:
        traversal_preorder(node.right, DFS_list)
    return DFS_list


if __name__ == '__main__':
    bst = BST()

    bst.insert(9)
    bst.insert(5)
    # bst.insert(35)
    bst.insert(15)
    bst.insert(25)
    bst.lookup(5)
    print("root", bst.root.value)
    print("left", bst.root.left)
    print("right", bst.root.right)
    print(bst.dfs_inorder())
    print(bst.dfs_preorder())
    print(bst.dfs_postorder())
    # print(bst.bfs_recursive([bst.root], []))
