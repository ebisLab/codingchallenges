arr = [1, 10, 18, 16, 88]


# create new method that will say reverse

"""ll are a list which are linked
starts at head and ends at tail

Look up: O(n)
Insert: O(n)
Delete: O(n)
Append: O(1)
Prepend: 0(1)


"""

# * define class node which will act as a blue print for each node


class Node():
    def __init__(self, data):  # we pass the data we want tthe node to hold
        self.data = data  # data passed is stored in self.data
        self.next = None  # pointer, always points to null or None


class LinkedList():
    def __init__(self):
        self.head = None  # when list is created, it is empty and ther is no node ot topoint to, so head will point to none at the time
        # since list is empty when created, we will point the tail to whatever the head is pointing to
        self.tail = self.head
        self.length = 0

    # ? Appending add nodes to the end of the LL
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
            self.tail.next = new_node  # next pointer of the last node  point to the new node
            self.tail = new_node  # update tail to point to the new node
            self.length += 1
            """
                ① ----▸ ②
                head    last node
                        tail
                --------
            #*  ① ----▸ ②  -----------▸ ③ 
            #*    head    last node *#   tail (pointer updated)    
            """

    # ? add node at the head of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        # update the head to point to the new node as we want the new node to be new first node (new head)
        self.head = new_node
        self.length += 1

    # ? print values in the nodes of the LL
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

    # def printThis(self):
    #     arr = []
    #     currNode = self.head
    #     while currNode is not None:
    #         arr.append(currNode.data)
    #         currNode = currNode.next
    #     return arr

    # ? this part allows us to insert data a specific position (even the middle)
    def insert(self, position, data):
        if position >= self.length:
            print("This position is not available. Insert at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        if position == 0:  # follow prepend position and add at head
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        if position < self.length:  # if position is in between, then we create a temp node which traverses the list upto the previous position of the position we want to enter the new node
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):  # traversale of the list its an O(n)
                current_node = current_node.next  # temp node
            # temp position and new node point to the same position --> we want to insert the new node here
            new_node.next = current_node.next
            current_node.next = new_node  # update next of the temp node to point to the new node
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
            self.length -= 1  # head gets disconnected from list
            return

        while current_node != None and current_node.next.data != data:
            # taverse list and check every node
            # loop until either the current node becomes NONE (end of the list) or until the data of the node next to the current node equals the data we want deleted
            current_node = current_node.next
        if current_node is not None:  # this would mean the next node of the current node is the one we want deleted
            current_node.next = current_node.next.next
            if current_node.next == None:
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
            self.length -= 1  # head gets disconnected from list
            return

        if position >= self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

    def reversing(self):
        if not self.head.next:
            return self.head

        first = self.head
        print("first", first, "self.head", self.head)
        self.tail = self.head
        second = first.next

        while second:  # as long as second is not null
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first


if __name__ == '__main__':
    ll = LinkedList()
    ll.print_list()

    # empty
    ll.append(1)
    ll.append(10)
    ll.append(18)
    ll.append(16)
    ll.append(88)
    ll.print_list()

    print("length of the list: ", ll.length)
    ll.reversing()
    ll.print_list()

    # ll.prepend(4)
    # ll.print_list()

    # ll.insert(2, 7)
    # ll.print_list()

    # ll.delete_by_value(7)
    # print("by val")
    # ll.print_list()

    # ll.delete_by_position(8)
    # print("by pos")
    # ll.print_list()

    # print("print this")

    # print(ll.head.data)
    # print(ll.tail.data)
