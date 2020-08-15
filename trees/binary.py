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


if __name__ == '__main__':
    bst = BST()

    # bst.print_list()

    bst.insert(9)
    bst.insert(5)
    # bst.insert(35)
    bst.insert(15)
    bst.insert(25)
    bst.lookup(5)
    print("root", bst.root.value)
    print("left", bst.root.left)
    print("right", bst.root.right)

    # s.push("Udemy")
    # s.push("google")
    # print(s.peek())
    # s.print_list()
    # s.pop()
    # s.print_list()

    # arr = StackArr()
    # # arr.peek()
    # print("print list")
    # arr.print_list2()
    # arr.push("Discord2")
    # arr.push("Udemy2")
    # print("printing from all", arr.array)
    # print("peeking", arr.peek())
    # # arr.peek()
    # print(arr.__dict__)
    # arr.print_list2()

    # arr.push("Slack")
    # arr.pop()
    # arr.print_list2()
