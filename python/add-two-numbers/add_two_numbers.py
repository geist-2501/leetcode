# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reg1 = 0
        reg2 = 0
        rem = 0
        tail = None
        head = None
        while l1 is not None or l2 is not None or rem != 0:
            if l1:
                reg1 = l1.val
                l1 = l1.next
            if l2:
                reg2 = l2.val
                l2 = l2.next

            total = reg1 + reg2 + rem
            single = total % 10
            rem = int((total - single) / 10)

            new_node = ListNode(single)

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            reg1 = 0
            reg2 = 0

        return head


