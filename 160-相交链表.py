# https://leetcode.cn/problems/intersection-of-two-linked-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        
        temp = headA
        while temp is not None:
            visited.add(temp)
            temp = temp.next
            
        temp = headB
        while temp is not None:
            if temp in visited:
                return temp
            temp = temp.next

        return None


if __name__ == "__main__":
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    print(Solution().getIntersectionNode(listA, listB))
