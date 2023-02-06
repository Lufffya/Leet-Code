# https://leetcode.cn/problems/binary-tree-preorder-traversal/

from typing import List, Optional
from helper import TreeNode, list_to_tree


# 递归法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root, res):
            if root is None:
                return
            res.append(root.val)
            traversal(root.left, res)
            traversal(root.right, res)

        res = []
        traversal(root, res)
        return res


# 迭代法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return res


if __name__ == "__main__":
    root = [1,None,2,3]
    root = list_to_tree(root)
    print(Solution().preorderTraversal(root))