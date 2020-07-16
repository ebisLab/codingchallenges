""" You're given a linked list, how would you reverse it"""

# * LinkedList: 3 ->5->45->3->7->0 null
# * null<-3<-5<-45<-3<-7<-0
# 1.  keep track of where my next is
# 2. Assigning the previous as a next
# 3. Assigning my current node to the previos
# value so that it can be used for the next iteration
# 4. Assign current node to temp

#  ? Looop through the linked list
# ? assign the next to the previous element
# ? last element assign it as a head, or return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # edge cases
        if head is None:
            return head

        node = head
        previous = None
        temp = None

        while node:
            # store the next in the temp variable
            temp = node.next  # we need to track where the next is
            # point previous to next
            node.next = previous

            # set the data for the next loop
            previous = node
            node = temp

        return previous


# TODO O(n) n is the the length of the linked list
# time complexity: O(n) -> we have to go through each node at least once
# * space complexity: O(1) -> no matter what happens we will always be defining variables
        # * as length increases there will always be the same variable pointing to the same place


# ! https://leetcode.com/problems/reverse-linked-list/submissions/


# TODO always ask for time complexity: How many times is the loop happening, in space, how many additional memories will I need. (will you still be defining the same variables regardless of how many nodes there are 1 or 1 million)
