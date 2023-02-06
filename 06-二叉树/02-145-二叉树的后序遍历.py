# https://leetcode.cn/problems/binary-tree-postorder-traversal/

from typing import List, Optional
from helper import TreeNode, list_to_tree


# 递归法
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


# 迭代法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return res[::-1]


if __name__ == "__main__":
    root = [3,1,2]
    root = list_to_tree(root)
    print(Solution().postorderTraversal(root))