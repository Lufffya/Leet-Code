# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### 初步设想 ###
# 思路: 先展开链表取值, 再排序并合并
# 不太优雅, 但能解
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_nums = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                list_nums.append(node.val)
                node = node.next
        list_nums.sort()
        re_node = ListNode()
        cur = re_node
        for i in range(len(list_nums)):
            cur.next = ListNode(list_nums[i])
            cur = cur.next
        return re_node.next


### Copilot ###
# 思路: 分治法, 太优雅了
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)


if __name__ == "__main__":
    lists  = [ListNode(1, ListNode(4, ListNode(5))),
              ListNode(1, ListNode(3, ListNode(4))),
              ListNode(2, ListNode(6))]
    print(Solution().mergeKLists(lists))
