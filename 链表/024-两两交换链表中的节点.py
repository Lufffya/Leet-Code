# https://leetcode.cn/problems/swap-nodes-in-pairs/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(next=head)
        cur = head
        while cur.next and cur.next.next:
            pass



        return head.next

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    r = Solution().swapPairs(head)
    print(r)