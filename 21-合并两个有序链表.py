# https://leetcode.cn/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### 初步设想 ###
# 思路: 先展开两个链表,组合并排序,再构建合并后的链表
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_nums, list2_nums = [], []
        while list1:
            list1_nums.append(list1.val)
            list1 = list1.next
        while list2:
            list2_nums.append(list2.val)
            list2 = list2.next
            
        list12_nums = (list1_nums + list2_nums)
        list12_nums.sort()
        re_node = ListNode()
        cur = re_node
        for i in range(len(list12_nums)):
            cur.next = ListNode(list12_nums[i])
            cur = cur.next
        return re_node.next


### Copilot ###
# 思路: 使用递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(list1, list2))
