from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        visited = set()
        pointer_a = head_a
        while pointer_a is not None:
            visited.add(pointer_a)
            pointer_a = pointer_a.next

        pointer_b = head_b
        while pointer_b is not None:
            if pointer_b in visited:
                break
            pointer_b = pointer_b.next

        return pointer_b
