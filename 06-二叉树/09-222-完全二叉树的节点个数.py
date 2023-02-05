# https://leetcode.cn/problems/count-complete-tree-nodes/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        left_depth = 1
        right_depth = 1

        root_left = root.left
        while root_left:
            left_depth +=1
            root_left = root_left.left

        root_right = root.right
        while root_right:
            right_depth +=1
            root_right = root_right.right
        
        if left_depth == right_depth:
            return (2 ** left_depth) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1


if __name__ == "__main__":
    aa = (2 << 1)

    root = [1,2,3,4,5,6]
    root = list_to_tree(root)
    print(Solution().countNodes(root))