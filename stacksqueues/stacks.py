class Node():
    def __init__(self, data):  # we pass the data we want tthe node to hold
        self.data = data  # data passed is stored in self.data
        self.next = None  # pointer, always points to null or None


class StackLL():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):  # lets us peek at the top of element without removing it from the stack
        return self.top.data

    def print_list(self):
        # check if its empty
        if self.top == None:
            print("Empty")
        else:
            current_node = self.top
            while current_node is not None:  # loop until the node we created becomes None
                print(current_node.data, end="-->")
                current_node = current_node.next
        print()
        return

        # temp = self.top
        # while temp is not None:
        #     print(temp.data, end='-->')
        #     temp = temp.next
        # print()

    def push(self, data):
        new_node = Node(data)
        if self.top is None:  # if stack is empty, we make the top and bottom pointer point to the new node
            self.top = new_node
            self.bottom = new_node
            self.length += 1
            return
        else:  # make the next of the new node which was pointing to None, point to the present top and then update the top pointer
            new_node.next = self.top
            self.top = new_node
            self.length += 1
            return

    def pop(self):
        pass

    def isEmpty(self):
        pass


if __name__ == '__main__':
    s = StackLL()

    s.print_list()
    # ll.print_list()

    s.push("Discord")
    s.push("Udemy")
    # s.push("google")
    # s.pop()
    s.print_list()
    # x = s.peek()
    # print(x)
