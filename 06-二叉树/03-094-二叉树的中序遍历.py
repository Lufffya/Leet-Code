# https://leetcode.cn/problems/binary-tree-inorder-traversal/

from typing import List, Optional
from helper import TreeNode, list_to_tree


# 递归法
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


# 迭代法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        cur = root
        stack = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
                
        return res


if __name__ == "__main__":
    root = [5,4,6,1,2]
    root = list_to_tree(root)
    print(Solution().inorderTraversal(root))