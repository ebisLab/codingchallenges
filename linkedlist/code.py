class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
#


def condense_linked_list(node):
    # utilizing tree traversal
    # node has to reference to head somehow
    # can this be sorted?
    # ||
    # \/
    # create empty set so that we can save the nodes we bring in
    # traverse until its not empty
    # if its seen the node before don't do anything
    # else: insert the current node into the set and go to the next

    prev = None
    curr = node
    print("we started")

    s = set()
    print(s, "set")

    while curr:
        print("inside curr")
        if curr.value in s:
            # node has been seen before
            prev.next = curr.next

        # GOAL: inserting node into set
        else:
            s.add(curr.value)
            prev = curr
        curr = prev.next
    return node


if __name__ == "__main__":
    x = [3, 4, 3, 2, 6, 1, 2, 6]
    node = None
    for i in range(len(x)):
        node = ListNode(x[i])  # node => next
    condense_linked_list(node)
    print("nodeing")

    print(node)

# https://www.techiedelight.com/remove-duplicates-linked-list/
