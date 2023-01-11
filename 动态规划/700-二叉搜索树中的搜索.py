# https://leetcode.cn/problems/search-in-a-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


if __name__ == "__main__":
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7))
    val = 5
    r = Solution().searchBST(root, val)
    print(r)
