from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "<{}>".format(self.val)

class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        forwards_q = [root]
        backwards_q = []

        layers = []

        while forwards_q != [] or backwards_q != []:
            going_forward = forwards_q != []
            current_q = forwards_q if going_forward else backwards_q
            other_q = backwards_q if going_forward else forwards_q

            for node in current_q:
                if node.left:
                    other_q.append(node.left)

                if node.right:
                    other_q.append(node.right)

            new_layer = list(map(lambda n: n.val, current_q))
            if not going_forward:
                new_layer.reverse()

            layers.append(new_layer)

            current_q.clear()

        return layers


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    print(s.zigzag_level_order(root))
