# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import Optional, List
from helper import TreeNode, list_to_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level = []
            size = len(queue)
            while size:
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

                size -= 1

            res.append(level)
        return res
    

if __name__ == "__main__":
    root = list_to_tree([3,4,7,1,3,5,8])
    print(Solution().levelOrder(root))
