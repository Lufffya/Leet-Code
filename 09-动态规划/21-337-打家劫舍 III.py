# https://leetcode.cn/problems/house-robber-iii/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    i = 1
    queue = [root]
    while queue:
        node = queue.pop(0)
        if i < len(nums):
            if nums[i]:
                node.left = TreeNode(nums[i])
                queue.append(node.left)
            i += 1
            
        if i < len(nums):
            if nums[i]:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1
    
    return root


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            
            if root is None:
                return (0, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)

            
            is_robed = root.val + left[1] + right[1]
            not_robed = max(left) + max(right)
            
            return (is_robed, not_robed)

        if not root:
            return 0
        
        return max(dfs(root))


if __name__ == '__main__':
    root = [3,2,3,None,3,None,1]
    root = list_to_tree(root)
    print(Solution().rob(root))