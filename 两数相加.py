# https://leetcode-cn.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
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
           
   
        
if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    Solution().addTwoNumbers(l1, l2)
    