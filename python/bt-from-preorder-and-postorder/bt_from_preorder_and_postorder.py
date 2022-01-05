# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} < {} | {} >".format(self.val, self.left, self.right)


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recurse(preorder, inorder)

    def recurse(self, preorder: List[int], inorder: List[int]):

        if len(preorder) != len(inorder):
            raise Exception("Array lengths are different")

        if len(preorder) == 0:
            return None

        root = preorder[0]
        index_root_inorder = inorder.index(root)

        left = self.recurse(preorder[1:index_root_inorder + 1], inorder[0:index_root_inorder])
        right = self.recurse(preorder[index_root_inorder + 1:], inorder[index_root_inorder + 1:])

        return TreeNode(root, left, right)


if __name__ == '__main__':
    s = Solution()
    print(s.build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
