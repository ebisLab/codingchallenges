"""
its better to not use array but to use LL
"""


class Node():
    def __init__(self, data):  # we pass the data we want tthe node to hold
        self.data = data  # data passed is stored in self.data
        self.next = None  # pointer, always points to null or None


class QueueLL():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):  # lets us peek at the first of element without removing it from the Queue
        return self.first.data

    def print_list(self):
        # check if its empty
        if self.first == None:
            print("Empty")
        else:
            current_node = self.first
            while current_node is not None:  # loop until the node we created becomes None
                print(current_node.data, end="-->")
                current_node = current_node.next
        print()
        return

    def enqueue(self, data):
        new_node = Node(data)  # instantiate new node with data
        if self.first is None:  # if Queue is empty, we make the first and last pointer point to the new node
            self.first = new_node
            self.last = new_node
            self.length += 1
            return
        else:  # make the next of the new node which was pointing to None, point to the present first and then update the first pointer
            new_node.next = self.first
            self.first = new_node
            self.length += 1
            return

    def dequeue(self):
        if self.first is None:
            print("Queue is empty")
            return
        else:
            self.first = self.first.next
            # print(self.length)
            self.length -= 1
            print(self.length)
            # we need to make the last pointer nONE if there's only 1 element
            if self.length == 0:
                self.last = None
            return

    def isEmpty(self):
        # print("leen", self.length)
        if self.length == 0:
            print(True)
            return True
        else:
            print(False)
            return False


if __name__ == '__main__':
    q = QueueLL()

    q.print_list()

    q.enqueue("Discord")
    q.enqueue("Udemy")
    q.enqueue("google")
    print(q.peek())
    q.print_list()
    q.dequeue()
    q.print_list()
    q.isEmpty()
