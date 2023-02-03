# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# list to tree
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