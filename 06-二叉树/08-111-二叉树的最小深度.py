# https://leetcode.cn/problems/minimum-depth-of-binary-tree/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if root.left is None and root.right is not None:
            return right_depth + 1

        if root.left is not None and root.right is None:
            return left_depth + 1

        return min(left_depth, right_depth) + 1


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    root = list_to_tree(root)
    print(Solution().minDepth(root))