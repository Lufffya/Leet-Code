# https://leetcode.cn/problems/binary-tree-postorder-traversal/

from typing import List, Optional
from helper import TreeNode, list_to_tree


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root, nums):
            if root is None:
                return
            traversal(root.left, nums)
            traversal(root.right, nums)
            nums.append(root.val)

        nums = []
        traversal(root, nums)
        return nums


if __name__ == "__main__":
    root = list_to_tree([3,1,2])
    print(Solution().postorderTraversal(root))