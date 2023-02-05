# https://leetcode.cn/problems/symmetric-tree/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(root_left, root_right):
            
            if root_left is None and root_right is None:
                return True

            elif root_left is None or root_right is None:
                return False

            elif root_left.val != root_right.val:
                return False
            
            if not compare(root_left.left, root_right.right):
                return False
            if not compare(root_left.right, root_right.left):
                return False

            return True

        if not root:
            return True
        return compare(root.left, root.right)


if __name__ == "__main__":
    root = [1,2,2,3,4,4,3]
    root = list_to_tree(root)
    print(Solution().isSymmetric(root))
