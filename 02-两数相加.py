# https://leetcode-cn.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### 初步设想 ###
# 思路: 先把两个链表转换成数组, 然后相加成一个数组, 接着为反置的数组使用递归的方式转换成链表
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num, l2_num = [], []
        while l1 is not None:
            l1_num.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_num.append(l2.val)
            l2 = l2.next
        
        l1_num = int(''.join([str(i) for i in l1_num[::-1]]))
        l2_num = int(''.join([str(i) for i in l2_num[::-1]]))
        sum_num = l1_num + l2_num
        re_num =  [int(i) for i in str(sum_num)][::-1]
        
        def recursion(node, num_list):
            node.val = num_list[0]
            if len(num_list) == 1: return node
            node.next = recursion(ListNode(), num_list[1:])
            return node
         
        return recursion(ListNode(), re_num) 
### 结果 ### 
# 执行用时: 72 ms, 在所有 Python3 提交中击败了 18.15% 的用户
# 内存消耗: 15 MB, 在所有 Python3 提交中击败了 43.29% 的用户


### Copilot ####
### 思路: 同时循环 l1 和 l2, 对位相加, 将和取模余数作为当前节点的值, 将和整除的结果(carry)作为下一节点的值, 然后将游标指向下一节点
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry: # 两个表链长度不同, 以及当最后一个carry不为0时
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
### 结果 ### 
# 执行用时: 64 ms, 在所有 Python3 提交中击败了 51.36% 的用户
# 内存消耗: 15 MB, 在所有 Python3 提交中击败了 61.14% 的用户


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    Solution().addTwoNumbers(l1, l2)
