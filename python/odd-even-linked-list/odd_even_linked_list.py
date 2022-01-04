# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        elif head.next is None:
            return head

        odd_head = head
        odd_tail = odd_head

        even_head = head.next
        even_tail = even_head

        while True:
            odd_is_behind = odd_head.next == even_head

            if odd_is_behind:
                next_head = even_head.next
                odd_head.next = next_head
                if next_head is None:
                    break
                odd_head = next_head
            else:
                next_head = odd_head.next
                even_head.next = next_head
                if next_head is None:
                    break
                even_head = next_head

        # Set OH to point to ET.

        odd_head.next = even_tail

        return odd_tail
