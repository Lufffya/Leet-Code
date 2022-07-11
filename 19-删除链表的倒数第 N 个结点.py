# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### 初步设想 ###
# 思路: 先把链表读出来, 在重建的时候跳过被标记为删除的节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_nums = []
        while head:
            head_nums.append(head.val)
            head = head.next
        n_i = len(head_nums) - n
        re_head = ListNode()
        cur = re_head
        for i in range(len(head_nums)):
            if i == n_i:
                continue
            cur.next = ListNode(head_nums[i])
            cur = cur.next
        return re_head.next
### 结果 ### 
# 执行用时: 40 ms, 在所有 Python3 提交中击败了 54.88% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 40.10% 的用户


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    n = 2
    print(Solution().removeNthFromEnd(head, n))
