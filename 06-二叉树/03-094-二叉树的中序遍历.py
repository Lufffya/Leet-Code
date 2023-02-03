# https://leetcode.cn/problems/binary-tree-inorder-traversal/

from typing import List, Optional
from helper import TreeNode, list_to_tree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root, nums):
            if root is None:
                return
            traversal(root.left, nums)
            nums.append(root.val)
            traversal(root.right, nums)

        nums = []
        traversal(root, nums)
        return nums


if __name__ == "__main__":
    root = list_to_tree([1,None,2,3])
    print(Solution().inorderTraversal(root))