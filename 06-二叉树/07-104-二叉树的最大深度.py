# https://leetcode.cn/problems/maximum-depth-of-binary-tree/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    root = list_to_tree(root)
    print(Solution().maxDepth(root))