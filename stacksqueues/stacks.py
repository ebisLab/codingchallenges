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
        if self.top is None:
            print("Stack is empty")
            return
        else:
            self.top = self.top.next
            # print(self.length)
            self.length -= 1
            print(self.length)
            # we need to make the bottom pointer nONE if there's only 1 element
            if self.length == 0:
                self.bottom = None
            return

    def isEmpty(self):
        pass


class StackArr():
    def __init__(self):
        self.array = []

    def peek(self):  # we need to access the last of the array (top)
        return self.array[len(self.array)-1]

        # print("self.arra", self.array[len(self.array)-1])

    def push(self, data):
        print("data", data)
        self.array.append(data)
        print(self.array)
        return

    def print_list2(self):
        print("--print list--")
        # print the last element of the list first
        # o(n)
        # print("self.array")
        # print(self.array)
        for i in range(len(self.array)):
            print(self.array[i])
        return

    def pop(self):
        if len(self.array) is not 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return


if __name__ == '__main__':
    s = StackLL()

    s.print_list()

    s.push("Discord")
    s.push("Udemy")
    s.push("google")
    print(s.peek())
    s.print_list()
    s.pop()
    s.print_list()

    arr = StackArr()
    # arr.peek()
    print("print list")
    arr.print_list2()
    arr.push("Discord2")
    arr.push("Udemy2")
    print("printing from all", arr.array)
    print("peeking", arr.peek())
    # arr.peek()
    print(arr.__dict__)
    arr.print_list2()

    arr.push("Slack")
    arr.pop()
    arr.print_list2()

    # x = s.peek()
    # print(x)
