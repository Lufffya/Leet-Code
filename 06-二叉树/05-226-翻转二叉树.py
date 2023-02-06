# https://leetcode.cn/problems/invert-binary-tree/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == "__main__":
    root = [4,2,7,1,3,6,9]
    root = list_to_tree(root)
    print(Solution().invertTree(root))