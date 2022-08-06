# https://leetcode.cn/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### Copilot ###
class Solution:
    # Reverse a one-way linked list using a circular method
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        cur = head
        pre = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre


### Copilot ###
class Solution:
    # Use the recursive method to reverse a one-way linked list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().reverseList(head))
