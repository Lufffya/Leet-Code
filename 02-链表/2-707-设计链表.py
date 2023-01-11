# https://leetcode.cn/problems/design-linked-list/


# 单链表
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.node = Node()
        self.node_len = 0

    def get(self, index: int) -> int:
        if self.node_len == 0 or index < 0 or index >= self.node_len:
            return -1
        count = 0
        cur = self.node
        while cur is not None:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.node_len == 0:
            self.node = Node(val)
        else:
            self.node = Node(val, self.node)
        self.node_len += 1

    def addAtTail(self, val: int) -> None:
        if self.node_len == 0:
            self.node = Node(val)
        else:
            cur = self.node
            while cur is not None:
                if cur.next is None:
                    cur.next = Node(val)
                    break
                cur = cur.next
        self.node_len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.node_len:
            self.addAtTail(val)
        elif index > self.node_len :
            return
        else:
            count = 0
            cur = self.node
            while cur.next is not None:
                if count == index-1:
                    cur.next = Node(val, cur.next)
                    self.node_len +=1
                    break
                cur = cur.next
                count += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.node_len:
            return
        if index == 0:
            self.node = self.node.next
            self.node_len -=1
            return
        if index == self.node_len-1:
            cur = self.node
            while cur.next is not None:
                if cur.next.next is None:
                    cur.next = None
                    self.node_len -=1
                    break
                cur = cur.next
            return

        count = 0
        cur = self.node
        while cur is not None:
            if count == index-1:
                cur.next = cur.next.next
                self.node_len -=1
                break
            cur = cur.next
            count += 1


if __name__ == "__main__":
    linkedList = MyLinkedList()
    methods = ["MyLinkedList","addAtIndex","get"]
    vales = [[],[1,0],[0]]
    
    for m, v in zip(methods[1:], vales[1:]):
        if m == "addAtHead":
            linkedList.addAtHead(v[0])
        elif m == "addAtTail":
            linkedList.addAtTail(v[0])
        elif m == "addAtIndex":
            linkedList.addAtIndex(v[0], v[1])
        elif m == "deleteAtIndex":
            linkedList.deleteAtIndex(v[0])
        elif m == "get":
            print(linkedList.get(v[0]))