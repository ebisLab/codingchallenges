"""dl are a list which are linked
starts at head and ends at tail

Look up: O(n)
Insert: O(n)
Delete: O(n)
Append: O(1)
Prepend: 0(1)


"""

# * define class node which widl act as a blue print for each node


class Node():
    def __init__(self, data):  # we pass the data we want tthe node to hold
        self.data = data  # data passed is stored in self.data
        self.next = None  # pointer, always points to nudl or None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None  # when list is created, it is empty and ther is no node ot topoint to, so head widl point to none at the time
        # since list is empty when created, we widl point the tail to whatever the head is pointing to
        self.tail = self.head
        self.length = 0

    # ? Appending add nodes to the end of the dl
    def append(self, data):  # creates a new instance of Node class
        new_node = Node(data)  # new node with info that user is inputing

        if self.head == None:  # check if its empty
            self.head = new_node  # point head to new node
            self.tail = self.head  # tail to the head
            self.length = 1
            """
                ▲
                |
                head and tail point to the same node

            """

        else:
            new_node.prev = self.tail
            self.tail.next = new_node  # next pointer of the last node  point to the new node
            self.tail = new_node  # update tail to point to the new node
            self.length += 1
            """
                ① ----▸ ②
                head    last node
                        tail
                --------
            # *  ① ----▸ ②  -----------▸ ③
            # *    head    last node *#   tail (pointer updated)
            """

    # ? add node at the head of the list
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.tail = self.head
            # update the head to point to the new node as we want the new node to be new first node (new head)
            self.head = new_node
            self.length += 1
            return
        else:
            new_node = self.head
            # 2-way link by making the previous of the present head point to the new node
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return

    # ? print values in the nodes of the dl
    def print_list(self):
        # check if its empty
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node is not None:  # loop until the node we created becomes None
                print(current_node.data, end=" ")
                current_node = current_node.next
        print()

    # ? this part adlows us to insert data a specific position (even the middle)
    def insert(self, position, data):
        if position == 0:
            # inserting at postion 0 is equivalent to prepending, so instead of repeating code, we simply cadl the prepend method
            self.prepend(data)
            return
        if position >= self.length:
            # inserting at postion >= the length of the list is equivalent to appending, we simply cadl the append method
            self.append(data)
            return

        else:  # if position is in between, then we create a temp node which traverses the list upto the previous position of the position we want to enter the new node
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):  # traversale of the list its an O(n)
                current_node = current_node.next  # temp node
            # temp position and new node point to the same position --> we want to insert the new node here
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next = new_node  # update next of the temp node to point to the new node
            new_node.prev = new_node
            self.length += 1
            return

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return
        current_node = self.head
        if current_node.data == data:  # if input val = head
            self.head = self.head.next  # head  -> input val
            if self.head == None or self.head.next == None:  # check if there's 1 or 0 nodes in the list
                # update tail to be equal to the head
                self.tail = self.head
            if self.head is not None:
                self.head.pre = None
            self.length -= 1  # head gets disconnected from list
            return

        while current_node != None and current_node.next.data != data:
            # taverse list and check every node
            # loop until either the current node becomes NONE (end of the list) or until the data of the node next to the current node equals the data we want deleted
            current_node = current_node.next
        if current_node is not None:  # this would mean the next node of the current node is the one we want deleted
            current_node.next = current_node.next.next
            if current_node.next is not None:  # if node not deleted is not the last node => the node ndext to the next to the urrent nod is ! - None
                # Then we set the prev of the node next to the deleted node equal to the current node, so a 2 way link is established
                current_node.next.prev = current_node
            else:
                # if the deleted node is the last node then we update the tail to be the current node
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Cant find value")
            return

    def delete_by_position(self, position):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return

        if position is 0:  # if input val = head
            self.head = self.head.next  # head  -> input val
            if self.head == None or self.head.next == None:  # check if there's 1 or 0 nodes in the list
                # update tail to be equal to the head
                self.tail = self.head
            if self.head is not None:
                self.head.prev is None  # we update the prev of the new head to be equal to None
            self.length -= 1  # head gets disconnected from list
            return

        if position >= self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next is not None:
            current_node.next.prev = current_node
        else:
            self.tail = current_node
        self.length -= 1

        return


if __name__ == '__main__':
    dl = DoublyLinkedList()
    # print(fullObj)

    dl.print_list()

    # empty
    dl.append(5)
    dl.append(2)
    dl.append(9)
    dl.print_list()

    print("length of the list: ", dl.length)

    dl.prepend(4)
    dl.print_list()
    print({f"head: {dl.head.data} tail: {dl.tail.data}"})

    dl.insert(2, 7)
    dl.print_list()
    print({f"head: {dl.head.data} tail: {dl.tail.data}"})

    dl.delete_by_value(2)
    dl.print_list()
    print({f"head: {dl.head.data} tail: {dl.tail.data}"})

    dl.delete_by_position(2)
    print("hold on")
    dl.print_list()
    print({f"head: {dl.head.data} tail: {dl.tail.data}"})
    # dl.printThis()

    # print(LinkedList())
