"""queue data structure, we can go back to the prev nodes and get its child nodes"""
"""
its better to not use array but to use LL
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

    def bfs(self):
        current_node = self.root
        # BFS_res=[]
        list_ = []
        queue = []  # keep track which level we're at

        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)  # extracting first node
            # print(current_node.value)
            list_.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return list_

    def bfs_recursive(self, queue, bfs_list):
        # base case when to stop
        if len(queue) == 0:
            return bfs_list
        currentnode = queue.pop(0)
        bfs_list.append(currentnode.value)

        if currentnode.left:
            queue.append(currentnode.left)
        if currentnode.right:
            queue.append(currentnode.right)
        return self.bfs_recursive(queue, bfs_list)


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
    print(bst.bfs())
    print(bst.bfs_recursive([bst.root], []))
