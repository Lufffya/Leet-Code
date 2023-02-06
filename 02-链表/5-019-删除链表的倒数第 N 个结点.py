# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        fast = head
        slow = head
        i = 0
        while fast:
            if i >= n+1:
                slow = slow.next
            fast = fast.next
            i += 1
            if fast is None:
                slow.next = slow.next.next

        return head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    r = Solution().removeNthFromEnd(head, n)
    print(r)