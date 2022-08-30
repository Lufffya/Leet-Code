# https://leetcode.cn/problems/symmetric-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if p is None and q is None:
                return True
    
            if p is None or q is None:
                return False
            
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)


if __name__ == "__main__":
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)), right=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3)))
    print(Solution().isSymmetric(root))

