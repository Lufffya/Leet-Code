# https://leetcode.cn/problems/balanced-binary-tree/

from typing import Optional
from helper import TreeNode, list_to_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(root):
            if root is None:
                return 0

            left_height = get_height(root.left)
            if left_height == -1:
                return -1
            right_height = get_height(root.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return get_height(root) != -1


if __name__ == "__main__":
    root = [1,2,2,3,None,None,3,4,None,None,4]
    root = list_to_tree(root)
    print(Solution().isBalanced(root))