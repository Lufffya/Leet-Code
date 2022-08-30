# https://leetcode.cn/problems/binary-tree-inorder-traversal/

from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res


if __name__ == "__main__":
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3)))
    print(Solution().inorderTraversal(root))
