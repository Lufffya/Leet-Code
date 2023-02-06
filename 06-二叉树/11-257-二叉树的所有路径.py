# https://leetcode.cn/problems/binary-tree-paths/

from typing import Optional, List
from helper import TreeNode, list_to_tree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def traversal(root, path, res):
            
            path.append(str(root.val))
            
            if root.left is None and root.right is None:
                res.append('->'.join(path))
            
            if root.left:
                traversal(root.left, path, res)
                path.pop()

            if root.right:
                traversal(root.right, path, res)
                path.pop()
            
        if root is None :
            return []
        path, res = [], []
        traversal(root, path, res)
        return res


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def traversal(root, path, res):
            
            path += str(root.val)
            
            if root.left is None and root.right is None:
                res.append(path)
            
            if root.left:
                traversal(root.left, path + '->', res)

            if root.right:
                traversal(root.right, path + '->', res)
            
        if root is None :
            return []
        res = []
        traversal(root, "", res)
        return res


if __name__ == "__main__":
    root = [1,2,3,None,5]
    root = list_to_tree(root)
    print(Solution().binaryTreePaths(root))