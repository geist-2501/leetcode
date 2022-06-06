# Medium interview collection.

# leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/
from typing import Optional

#      A     1st 2^0 `if iter == 2 ** (curr_layer - 1) then push layer and create new, curr_layer++`
#   B    C   2nd 2^1
#  D E  F G  4th 2^2
# ...        8th
#            16th

# DS: DEFG

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    def show(self) -> str:
        return f"[{self.val}, {self.left.show() if self.left else 'none'} | {self.right.show() if self.right else 'none'}]"


class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        # Transform tree into collection of array layers.
        queue = [root]
        node_idx = 0
        curr_layer_idx = 1
        curr_layer = None
        layers = []
        while len(queue) > 0:
            node = queue.pop(0)
            node_idx += 1
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if node_idx == 2 ** (curr_layer_idx - 1):
                # New layer.
                if curr_layer:
                    layers.append(curr_layer)
                curr_layer = []
                curr_layer_idx += 1

            curr_layer.append(node)

        # Add final layer.
        layers.append(curr_layer)

        # Re-route the nodes in each layer.
        for layer in layers:
            for i in range(len(layer)):
                next_node = layer[i + 1] if i < len(layer) - 1 else None
                layer[i].next = next_node

        return root


class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root



if __name__ == '__main__':
    root = Node(1,
                left=Node(2,
                          left=Node(4),
                          right=Node(5)),
                right=Node(3,
                           left=Node(6),
                           right=Node(7)))
    s = Solution2()
    print(s.connect(root).show())
