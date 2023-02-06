# https://leetcode.cn/problems/sum-of-left-leaves/comments/

from typing import Optional, List
from helper import TreeNode, list_to_tree


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)

        cur_left_leaves = 0

        if root.left is not None and root.left.left is None and root.left.right is None:
            cur_left_leaves += root.left.val

        return left_sum + right_sum + cur_left_leaves # 中


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7] 
    root = list_to_tree(root)
    print(Solution().sumOfLeftLeaves(root))